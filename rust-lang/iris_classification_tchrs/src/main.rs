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
use tch::{kind, Kind, Tensor, no_grad, vision};

static IMAGE_DIM: i64 = 784;
static LABELS: i64 = 1;

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
    let test_size: f64 = 0.5;
    let test_size: f64 = data.len() as f64 * test_size;
    let test_size = test_size.round() as usize;
    let feature_length = 4;

    let (test_data, train_data) = data.split_at(test_size);
    let train_size = train_data.len();
    let test_size = test_data.len();
    assert_eq!(train_size, test_size);

    // differentiate the features and the labels.
    // torch needs vectors in f64
    let flower_x_train: Vec<f64> = train_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_train: Vec<f64> = train_data.iter().map(|r| r.into_labels()).collect();

    let flower_x_test: Vec<f64> = test_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_test: Vec<f64> = test_data.iter().map(|r| r.into_labels()).collect();

    let flower_x_train = Tensor::float_vec(flower_x_train.as_slice());
    let flower_y_train = Tensor::float_vec(flower_y_train.as_slice()).to_kind(Kind::Int64);
    let flower_x_test = Tensor::float_vec(flower_x_test.as_slice());
    let flower_y_test = Tensor::float_vec(flower_y_test.as_slice()).to_kind(Kind::Int64);

    // print shape of all the data.
    println!("Training data shape {:?}", flower_x_train.size());
    println!("Training flower_y_train data shape {:?}", flower_y_train.size());

    // reshaping examples
    // one way to reshape is using unsqueeze
    //let flower_x_train1 = flower_x_train.unsqueeze(0); // Training data shape [1, 360]
    //println!("Training data shape {:?}", flower_x_train1.size());
    let train_size = train_size as i64;
    let test_size = test_size as i64;
    let flower_x_train = flower_x_train.view(&[train_size, feature_length]);
    let flower_x_test = flower_x_test.view(&[test_size, feature_length]);
    let flower_y_train = flower_y_train.view(&[train_size]);
    let flower_y_test = flower_y_test.view(&[test_size]);

    let mut ws = Tensor::rand(&[feature_length, 1], kind::FLOAT_CPU).set_requires_grad(true);
    let mut bs = Tensor::rand(&[train_size], kind::FLOAT_CPU).set_requires_grad(true);


    for epoch in 1..200 {
        let logits = flower_x_train.mm(&ws) + &bs;
        let loss = logits.squeeze().cross_entropy_for_logits(&flower_y_train); // since working on label encoded vectors.
        ws.zero_grad();
        bs.zero_grad();
        loss.backward();
        no_grad(|| {
            ws += ws.grad() * (-1);
            bs += bs.grad() * (-1);
        });
        let test_logits = flower_x_test.mm(&ws) + &bs;
        let test_accuracy = test_logits
            .argmax1(-1, false)
            .eq1(&flower_y_test)
            .to_kind(Kind::Float)
            .mean()
            .double_value(&[]);
        println!(
            "epoch: {:4} train loss: {:8.5} test acc: {:5.2}%",
            epoch,
            loss.double_value(&[]),
            100. * test_accuracy
        );
    }

    Ok(())
}
