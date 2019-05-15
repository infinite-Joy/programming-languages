extern crate tch;

use std::process::exit;
use std::env::args;
use std::io;
use std::fs::{self, DirEntry, copy, create_dir_all};
use std::path::Path;

use tch::{Device, Tensor, nn};
use tch::nn::{ModuleT, OptimizerConfig, conv2d, linear};
use tch::vision::imagenet::load_from_dir;
use failure;

// for the CNN
const BATCH_SIZE: i64 = 32;
const LABELS: i64 = 102;

const W: i64 = 224;
const H: i64 = 224;
const C: i64 = 3;

// for the simple nn
const IMAGE_DIM: i64 = W * W * C;
const HIDDEN_NODES: i64 = 128;

const DATASET_FOLDER: &str = "dataset";

fn visit_dir(dir: &Path, train_fn: &Fn(&DirEntry), test_fn: &Fn(&DirEntry)) -> io::Result<()> {
    if dir.is_dir() {
        let mut this_label = String::from("");
        for entry in fs::read_dir(dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.is_dir() {
                visit_dir(&path, train_fn, test_fn)?;
            } else {
                let full_path: Vec<String> = path.to_str().unwrap()
                    .split("/").into_iter()
                    .map(|x| x[..].to_string()).collect();
                if this_label == full_path[1] {
                    train_fn(&entry); // move the training file
                } else {
                    test_fn(&entry); // move the testing file
                }
                // the second entry is the label
                this_label = full_path[1].clone();
            }
        }
    }
    Ok(())
}

fn print_directory(dir: &Path) {
    println!("{:?}", dir);
}

fn move_file(from_path: &DirEntry, to_path: &Path) -> io::Result<()> {
    let root_folder = Path::new(DATASET_FOLDER);
    let second_order = root_folder.join(to_path);
    let full_path: Vec<String> = from_path.path().to_str().unwrap()
        .split("/").into_iter().map(|x| x[..].to_string()).collect();
    let label = full_path[1].clone();
    let third_order = second_order.join(label);
    create_dir_all(&third_order)?;
    let filename = from_path.file_name();
    let to_filename = third_order.join(&filename);
    // println!("{:?}", to_filename);
    copy(from_path.path(), to_filename)?;
    Ok(())
}

// image dataset: http://www.vision.caltech.edu/Image_Datasets/Caltech101/

#[derive(Debug)]
struct CnnNet {
    conv1: nn::Conv2D,
    conv2: nn::Conv2D,
    fc1: nn::Linear,
    fc2: nn::Linear,
}

impl CnnNet {
    fn new(vs: &nn::Path) -> CnnNet {
        let conv1 = conv2d(vs, C, 32, 5, Default::default());
        let conv2 = conv2d(vs, 32, 64, 5, Default::default());
        let fc1 = linear(vs, 1024, 1024, Default::default());
        let fc2 = linear(vs, 1024, LABELS, Default::default());
        CnnNet {
            conv1,
            conv2,
            fc1,
            fc2,
        }
    }
}

impl nn::ModuleT for CnnNet {
    fn forward_t(&self, xs: &Tensor, train: bool) -> Tensor {
        xs.view(&[-1, C, H, W])
            .apply(&self.conv1)
            .max_pool2d_default(2)
            .apply(&self.conv2)
            .max_pool2d_default(2)
            .view(&[-1, 1024])
            .apply(&self.fc1)
            .relu()
            .dropout_(0.5, train)
            .apply(&self.fc2)
    }
}

#[derive(Debug)]
struct SimpleNN {
    fc1: nn::Linear,
    fc2: nn::Linear,
}

impl SimpleNN {
    fn new(vs: &nn::Path) -> SimpleNN {
        let fc1 = linear(vs / "layer1", 224, HIDDEN_NODES, Default::default());
        let fc2 = linear(vs, HIDDEN_NODES, LABELS, Default::default());
        SimpleNN {
            fc1,
            fc2,
        }
    }
}

impl nn::ModuleT for SimpleNN {
    fn forward_t(&self, xs: &Tensor, train: bool) -> Tensor {
        let t = xs.view(&[-1, W]);
        println!("{:?}", t.size());
        let a = t.apply(&self.fc1);
        println!("{:?}", a.size());
        let mut b = a.relu();
        println!("{:?}", b.size());
        let c = b.dropout_(0.5, train);
        println!("{:?}", c.size());
        let d = c.apply(&self.fc2);
        println!("{:?}", d.size());
        d
        // xs.apply(&self.fc1)
        //     .relu()
        //     .dropout_(0.5, train)
        //     .apply(&self.fc2)
    }
}

fn learning_rate(epoch: i64) -> f64 {
    if epoch < 10 {
        0.1
    } else if epoch < 20 {
        0.01
    } else {
        1e-4
    }
}

fn main() -> failure::Fallible<()> {
    let args: Vec<String> = args().collect();
    let create_directories = if args.len() < 2 {
        None
    } else {
        Some(args[1].as_str())
    };
    match create_directories {
        None => (),
        Some("yes") => {
            let obj_categories = Path::new("101_ObjectCategories");
            let move_to_train = |x: &DirEntry| {
               let to_folder = Path::new("train");
               move_file(&x, &to_folder).unwrap();
            };
            let move_to_test =
                |x: &DirEntry| {
                    let to_folder = Path::new("val");
                    move_file(&x, &to_folder).unwrap();
                };
            visit_dir(
                &obj_categories, &move_to_train, &move_to_test).unwrap();
        },
        Some(_) => {
            println!("Usage: cargo run yes", );
            exit(1)
        },
    }
    println!("files kept in the imagenet format in {}", DATASET_FOLDER);
    println!("moving on with training.");
    let image_dataset = load_from_dir(DATASET_FOLDER).unwrap();
    let vs = nn::VarStore::new(Device::cuda_if_available());
    // let net = Net::new(&vs.root());
    let net = SimpleNN::new(&vs.root());
    for epoch in 1..100 {
        let opt = nn::Adam::default().build(&vs, learning_rate(epoch))?;
        for (bimages, blabels) in image_dataset.train_iter(BATCH_SIZE).shuffle().to_device(vs.device()) {
            let loss = net
                .forward_t(&bimages, true)
                .cross_entropy_for_logits(&blabels);
            opt.backward_step(&loss);
        }
        let test_accuracy =
            net.batch_accuracy_for_logits(&image_dataset.test_images,
                                          &image_dataset.test_labels,
                                          vs.device(), 1024);
        println!("epoch: {:4} test acc: {:5.2}%",
            epoch, 100. * test_accuracy,);
    }
    println!("Training done!");
    Ok(())
}
