extern crate tch;

use std::io::{BufReader, Read, Result};
use std::error::Error;
use std::io;
use std::fs::{self, DirEntry, copy, create_dir_all};
use std::path::Path;


use tch::{kind, nn, nn::OptimizerConfig, Device, Kind, Tensor};
// use tch::vision::dataset::Dataset;
// use tch::vision::image::load_dir;
// use tch::vision::image::load_and_resize;
use tch::vision::imagenet::load_from_dir;

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





fn main() {
    // let device = Device::cuda_if_available();
    // let image_tensor = load_dir("101_ObjectCategories", 50, 50).unwrap();
    // let image_tensor = load_dir("test_image_dir", 50, 50).unwrap();
    // let image_dataset = load_from_dir("test_image_dir").unwrap();
    // println!("{:?}", image_dataset);




    // let obj_categories = Path::new("101_ObjectCategories");
    // let obj_categories = Path::new("test_folder");
    // let move_to_train = |x: &DirEntry| {
    //     let to_folder = Path::new("train");
    //     move_file(&x, &to_folder).unwrap();
    // };
    // let move_to_test = |x: &DirEntry| {
    //     let to_folder = Path::new("val");
    //     move_file(&x, &to_folder).unwrap();
    // };
    // create_train_val_folders(&obj_categories, &move_to_train, &move_to_test).unwrap();
    let image_dataset = load_from_dir(DATASET_FOLDER).unwrap();
    println!("{:?}", image_dataset);
    println!("Hello, world!");
}
