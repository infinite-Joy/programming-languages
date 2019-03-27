extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;

use std::io;
use std::process;
use std::vec::Vec;
use std::error::Error;

use csv;
use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;

use tch;
use tch::{kind, Tensor};

fn main() {
    if let Err(err) = read_csv() {
        println!("{}", err);
        process::exit(1);
    }
}

#[derive(Debug, Deserialize)]
struct Flower {
    sepal_length: f64, // everything needs to be f64 for torch.
    sepal_width: f64,
    petal_length: f64,
    petal_width: f64,
    species: String,
}

impl Flower {
    fn into_feature_vector(&self) -> Vec<f64> {
        vec![self.sepal_length, self.sepal_width, self.sepal_length, self.petal_width]
    }

    fn into_labels(&self) -> f64 {
        match self.species.as_str() {
            "setosa" => 0.,
            "versicolor" => 1.,
            "virginica" => 2.,
            l => panic!("Not able to parse the label. Some other label got passed. {:?}", l),
        }
    }
}

fn read_csv() -> Result<(), Box<Error>> {
    // Get all the data
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut data = Vec::new();
    for result in rdr.deserialize() {
        let r: Flower = result?;
        data.push(r); // data contains all the records
    }

    // shuffle the data.
    data.shuffle(&mut thread_rng());

    // separate out to train and test datasets.
    let test_size: f64 = 0.2;
    let test_size: f64 = data.len() as f64 * test_size;
    let test_size = test_size.round() as usize;
    // we are keeping the val size to be the same as test_size.
    // this can be changed if required
    let val_size  = test_size.clone();

    let (test_data, train_and_val_data) = data.split_at(test_size);
    let (val_data, train_data) = train_and_val_data.split_at(val_size);
    let train_size = train_data.len();
    let test_size = test_data.len();
    let val_size = val_data.len();

    // differentiate the features and the labels.
    // torch needs vectors in f64
    let flower_x_train: Vec<f64> = train_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    // let flower_y_train: Vec<f64> = train_data.iter().map(|r| r.into_labels()).collect();

    // let flower_x_test: Vec<f64> = test_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    // let flower_y_test: Vec<f64> = test_data.iter().map(|r| r.into_labels()).collect();

    // let flower_x_val: Vec<f64> = val_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    // let flower_y_val: Vec<f64> = val_data.iter().map(|r| r.into_labels()).collect();

    // let t = Tensor::float_vec(flower_x_train.as_slice());
    let mut t = Tensor::float_vec(&vec![1.1, 2.1, 3.1]);
    t.print();
    // let t = Tensor::randn(&[5, 4], kind::FLOAT_CPU);
    // t.print();
    // (&t + 1.5).print();
    // (&t + 2.5).print();
    // let mut t = Tensor::float_vec(&vec![1.1, 2.1, 3.1]); // so loading from a vector works.
    // // let mut t = Tensor::float_vec(&[1.1, 2.1, 3.1]);
    // t += 42;
    // t.print();
    // println!("{:?} {}", t.size(), t.double_value(&[1]));



    Ok(())
}