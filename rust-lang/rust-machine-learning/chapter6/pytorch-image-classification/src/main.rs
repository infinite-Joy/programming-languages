extern crate tch;

use std::io::{BufReader, Read, Result};
use std::error::Error;
use std::io;
use std::fs::{self, DirEntry, copy, create_dir_all};
use std::path::Path;


use tch::{kind, nn, nn::OptimizerConfig, Device, Kind, Tensor};
use tch::nn::{FuncT, ModuleT, SequentialT};
// use tch::vision::dataset::Dataset;
// use tch::vision::image::load_dir;
// use tch::vision::image::load_and_resize;
use tch::vision::imagenet::load_from_dir;
use failure;

const IMG_SIZE: i64 = 64;
const LATENT_DIM: i64 = 128;
const BATCH_SIZE: i64 = 32;
const LEARNING_RATE: f64 = 1e-4;
const BATCHES: i64 = 100000000;

const W: i64 = 32;
const H: i64 = 32;
const C: i64 = 3;
const BYTES_PER_IMAGE: i64 = W * H * C + 1;
const SAMPLES_PER_FILE: i64 = 10000;

const DATASET_FOLDER: &str = "dataset";

// one possible implementation of walking a directory only visiting files
fn create_train_val_folders(dir: &Path, train_fn: &Fn(&DirEntry), test_fn: &Fn(&DirEntry)) -> io::Result<()> {
    if dir.is_dir() {
        let mut this_label = String::from("");
        for entry in fs::read_dir(dir)? {
            let entry = entry?;
            let path = entry.path();
            if path.is_dir() {
                create_train_val_folders(&path, train_fn, test_fn)?;
            } else {
                let full_path: Vec<String> = path.to_str().unwrap()
                    .split("/").into_iter()
                    .map(|x| x[..].to_string()).collect();
                println!("{:?}", this_label);
                println!("{:?}", full_path);
                if this_label == full_path[1] {
                    train_fn(&entry); // move the training file
                } else {
                    test_fn(&entry); // move the testing file
                }
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
    let highest_folder = Path::new(DATASET_FOLDER);
    let second_order = highest_folder.join(to_path);
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

// pub fn load_dir<T: AsRef<Path>>(path: T, out_w: i64, out_h: i64) -> Tensor {
//     let mut files: Vec<std::fs::DirEntry> = vec![];
//     visit_dirs(&path.as_ref(), &mut files)?;
//     println!("{:?}", files);
//     ensure!(!files.is_empty(), "no image found in {:?}", path.as_ref());
//     let v: Vec<_> = files
//         .iter()
//         // Silently discard image errors.
//         .filter_map(|x| load_and_resize(x.path(), out_w, out_h).ok())
//         .collect();
//     Ok(Tensor::stack(&v, 0))
// }



// fn conv_bn(vs: &nn::Path, c_in: i64, c_out: i64) -> SequentialT {
//     let conv2d_cfg = nn::ConvConfig {
//         padding: 1,
//         bias: false,
//         ..Default::default()
//     };
//     nn::seq_t()
//         .add(nn::conv2d(vs, c_in, c_out, 3, conv2d_cfg))
//         .add(nn::batch_norm2d(vs, c_out, Default::default()))
//         .add_fn(|x| x.relu())
// }

#[derive(Debug)]
struct Net {
    conv1: nn::Conv2D,
    conv2: nn::Conv2D,
    fc1: nn::Linear,
    fc2: nn::Linear,
}

impl Net {
    fn new(vs: &nn::Path) -> Net {
        let conv1 = nn::conv2d(vs, 1, 32, 2, Default::default());
        let conv2 = nn::conv2d(vs, 32, 64, 2, Default::default());
        let fc1 = nn::linear(vs, 1024, 1024, Default::default());
        let fc2 = nn::linear(vs, 1024, 4, Default::default());
        Net {
            conv1,
            conv2,
            fc1,
            fc2,
        }
    }
}

impl nn::ModuleT for Net {
    fn forward_t(&self, xs: &Tensor, train: bool) -> Tensor {
        xs.view(&[-1, 1, 224, 224])
            .apply(&self.conv1)
            .max_pool2d_default(2)
            // .apply(&self.conv2)
            // .max_pool2d_default(2)
            .view(&[-1, 512])
            .apply(&self.fc1)
            .relu()
            .dropout_(0.5, train)
            .apply(&self.fc2)
    }
}

fn conv_bn(vs: &nn::Path, c_in: i64, c_out: i64) -> SequentialT {
    let conv2d_cfg = nn::ConvConfig {
        padding: 1,
        bias: false,
        ..Default::default()
    };
    nn::seq_t()
        .add(nn::conv2d(vs, c_in, c_out, 3, conv2d_cfg))
        .add(nn::batch_norm2d(vs, c_out, Default::default()))
        .add_fn(|x| x.relu())
}

fn layer<'a>(vs: &nn::Path, c_in: i64, c_out: i64) -> FuncT<'a> {
    let pre = conv_bn(&vs.sub("pre"), c_in, c_out);
    let block1 = conv_bn(&vs.sub("b1"), c_out, c_out);
    let block2 = conv_bn(&vs.sub("b2"), c_out, c_out);
    nn::func_t(move |xs, train| {
        let pre = xs.apply_t(&pre, train).max_pool2d_default(2);
        let ys = pre.apply_t(&block1, train).apply_t(&block2, train);
        pre + ys
    })
}

// fn fast_resnet(vs: &nn::Path) -> SequentialT {
//     nn::seq_t()
//         .add(conv_bn(&vs.sub("pre"), 3, 64))
//         .add(layer(&vs.sub("layer1"), 64, 128))
//         .add(conv_bn(&vs.sub("inter"), 128, 256))
//         .add_fn(|x| x.max_pool2d_default(2))
//         .add(layer(&vs.sub("layer2"), 256, 512))
//         .add_fn(|x| x.max_pool2d_default(4).flat_view())
//         .add(nn::linear(&vs.sub("linear"), 512, 10, Default::default()))
//         .add_fn(|x| x * 0.125)
// }

fn fast_resnet(vs: &nn::Path) -> SequentialT {
    nn::seq_t()
        .add(conv_bn(&vs.sub("pre"), 3, 32))
        // .add(layer(&vs.sub("layer1"), 32, 64))
        // .add(conv_bn(&vs.sub("inter"), 128, 256))
        .add_fn(|x| x.max_pool2d_default(2))
        .add_fn_t(|xs, train| xs.dropout(0.5, train))
        // .add(layer(&vs.sub("layer2"), 64, 128))
        // .add_fn(|x| x.max_pool2d_default(2))
        .add(nn::linear(&vs.sub("linear"), 512, 4, Default::default()))
        // .add_fn(|x| x * 0.125)
}

fn learning_rate(epoch: i64) -> f64 {
    if epoch < 50 {
        0.1
    } else if epoch < 100 {
        0.01
    } else {
        0.001
    }
}





fn main() -> failure::Fallible<()> {
    // let device = Device::cuda_if_available();
    // let image_tensor = load_dir("101_ObjectCategories", 50, 50).unwrap();
    // let image_tensor = load_dir("test_image_dir", 50, 50).unwrap();
    // let image_dataset = load_from_dir("test_image_dir").unwrap();
    // println!("{:?}", image_dataset);




    //let obj_categories = Path::new("101_ObjectCategories");
    //let move_to_train = |x: &DirEntry| {
    //    let to_folder = Path::new("train");
    //    move_file(&x, &to_folder).unwrap();
    //};
    //let move_to_test = |x: &DirEntry| {
    //    let to_folder = Path::new("val");
    //    move_file(&x, &to_folder).unwrap();
    //};
    //create_train_val_folders(&obj_categories, &move_to_train, &move_to_test).unwrap();
    let image_dataset = load_from_dir(DATASET_FOLDER).unwrap();
    let vs = nn::VarStore::new(Device::cuda_if_available());
    // let net = fast_resnet(&vs.root());
    // let mut opt = nn::Sgd {
    //     momentum: 0.9,
    //     dampening: 0.,
    //     wd: 5e-4,
    //     nesterov: true,
    // }.build(&vs, 0.)?;
    // for epoch in 1..150 {
    //     opt.set_lr(learning_rate(epoch));
    //     for (bimages, blabels) in image_dataset
    //         .train_iter(64).shuffle().to_device(vs.device()) {
    //         let bimages = tch::vision::dataset::augmentation(
    //             &bimages, true, 4, 8);
    //         println!("{:?}", bimages.size());
    //         // let loss = net
    //         //     .forward_t(&bimages, true)
    //         //     .cross_entropy_for_logits(&blabels);
    //     //     opt.backward_step(&loss);
    //     }
    //     // let test_accuracy =
    //     //     net.batch_accuracy_for_logits(
    //     //         &image_dataset.test_images,
    //     //         &image_dataset.test_labels, 
    //     //         vs.device(), 512);
    //     // println!("epoch: {:4} test acc: {:5.2}%", epoch, 100. * test_accuracy,);
    // }
    // println!("{:?}", image_dataset);

    let net = Net::new(&vs.root());
    let opt = nn::Adam::default().build(&vs, 1e-4)?;
    for epoch in 1..100 {
        for (bimages, blabels) in image_dataset.train_iter(1).shuffle().to_device(vs.device()) {
        // for (bimages, blabels) in image_dataset.train_iter(4).shuffle().to_device(vs.device()) {
            // println!("{:?}", bimages.size());
            // println!("{:?}", blabels.size());
            let loss = net
                .forward_t(&bimages, true)
                .cross_entropy_for_logits(&blabels);
            opt.backward_step(&loss);
            print!(".")
        }
        let test_accuracy =
            net.batch_accuracy_for_logits(&image_dataset.test_images, &image_dataset.test_labels, vs.device(), 1024);
        println!("epoch: {:4} test acc: {:5.2}%", epoch, 100. * test_accuracy,);
    }












    println!("Hello, world!");
    Ok(())
}
