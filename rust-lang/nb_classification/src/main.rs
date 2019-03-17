use std::io;
use std::process;
use std::vec::Vec;
// use std::io::{Read, Write};
// use std::path::Path;
// use std::fs::File;
// use std::io::{BufRead, BufReader};
use std::error::Error;
extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;


// use hyper;
// use hyper::client::Client;
use rusty_machine;
use rusty_machine::linalg::{Matrix, BaseMatrix};
use rusty_machine::linalg::Vector as rm_vector;
use rusty_machine::learning::naive_bayes::{self, NaiveBayes};
use rusty_machine::learning::SupModel;
// use rulinalg;
// use rulinalg::io::csv::{Reader, Writer};
use csv;

fn main() {
    if let Err(err) = read_csv() {
        println!("{}", err);
        process::exit(1);
    }
}

#[derive(Debug, Deserialize)]
struct Flower {
    sepal_length: f64, // everything needs to be f64, other types wont do in rusty machine
    sepal_width: f64,
    petal_length: f64,
    petal_width: f64,
    species: String,
}

impl Flower {
    fn into_feature_vector(&self) -> Vec<f64> {
        let x_vector = vec![self.sepal_length, self.sepal_width, self.sepal_length, self.petal_width];
        x_vector
    }

    fn into_labels(&self) -> Vec<f64> {
        match self.species.as_str() {
            "setosa" => vec![1., 0., 0.],
            "versicolor" => vec![0., 1., 0.],
            "virginica" => vec![0., 0., 1.],
            l => panic!("Not able to parse the label. Some other label got passed. {:?}", l),
        }
    }
}


fn read_csv() -> Result<(), Box<Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut flower_matrix = Vec::new();
    let mut labels = Vec::new();
    for result in rdr.deserialize() {
        let r: Flower = result?;
        flower_matrix.extend(r.into_feature_vector());
        labels.extend(r.into_labels());
    }

    let flower_matrix = Matrix::new(150, 4, flower_matrix);
    let labels = labels.chunks(3).collect();

    let mut model = NaiveBayes::<naive_bayes::Bernoulli>::new();
    model.train(&flower_matrix, &labels)
        .expect("failed to train model of dogs");

    // How many classes do I h ave?
    println!("{:?}", model.class_prior());

    // Creating some dummy test data.
    let test_matrix = Matrix::ones(1, 4);
    let predictions = model.predict(&test_matrix)
        .expect("Failed to predict");
    println!("{:?}", predictions);

    Ok(())
}