extern crate tch;

use std::io::{BufReader, Read, Result};
use std::error::Error;

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
    let device = Device::cuda_if_available();
    // let image_tensor = load_dir("101_ObjectCategories", 50, 50).unwrap();
    // let image_tensor = load_dir("test_image_dir", 50, 50).unwrap();
    let image_dataset = load_from_dir("test_image_dir").unwrap();
    println!("{:?}", image_dataset);
    println!("Hello, world!");
}
