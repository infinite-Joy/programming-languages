extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;

use std::io;
use std::process;
use std::vec::Vec;
use std::error::Error;

use rusty_machine;
use rusty_machine::linalg::{Matrix, BaseMatrix};
use rusty_machine::linalg::Vector;
// use rusty_machine::learning::glm::{Bernoulli, GenLinearModel};
use rusty_machine::learning::naive_bayes::{NaiveBayes, Gaussian, Bernoulli};
use rusty_machine::learning::SupModel;
use rusty_machine::analysis::score::accuracy;
use csv;
use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;

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
        vec![self.sepal_length, self.sepal_width, self.sepal_length, self.petal_width]
    }

    fn into_labelencoded_labels(&self) -> f64 {
        match self.species.as_str() {
            "setosa" => 0.,
            "versicolor" => 1.,
            "virginica" => 2.,
            l => panic!("Not able to parse the label. Some other label got passed. {:?}", l),
        }
    }

    fn into_onehot_labels(&self) -> Vec<f64> {
        match self.species.as_str() {
            "setosa" => vec![1., 0., 0.],
            "versicolor" => vec![0., 1., 0.],
            "virginica" => vec![0., 0., 1.],
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
    let (test_data, train_data) = data.split_at(test_size);
    let train_size = train_data.len();
    let test_size = test_data.len();

    // differentiate the features and the labels.
    let flower_x_train: Vec<f64> = train_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_train_lc: Vec<f64> = train_data.iter().map(|r| r.into_labelencoded_labels()).collect();
    let flower_y_train_onehot: Vec<f64> = train_data.iter().flat_map(|r| r.into_onehot_labels()).collect();

    let flower_x_test: Vec<f64> = test_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_test_lc: Vec<f64> = test_data.iter().map(|r| r.into_labelencoded_labels()).collect();
    let flower_y_test_onehot: Vec<f64> = test_data.iter().flat_map(|r| r.into_onehot_labels()).collect();

    // COnvert the data into matrices for rusty machine
    let flower_x_train = Matrix::new(train_size, 4, flower_x_train);
    let flower_y_train_lc = Vector::new(flower_y_train_lc);
    let flower_y_train_onehot = Matrix::new(train_size, 3, flower_y_train_onehot);
    let flower_x_test = Matrix::new(test_size, 4, flower_x_test);
    let flower_y_test_lc = Vector::new(flower_y_test_lc);
    // let flower_y_test_onehot = Matrix::new(test_size, 3, flower_y_test_onehot);

    // // Create GLM with Bernoulli distribution.
    // let mut model_glm_bernoulli = GenLinearModel::new(Bernoulli);
    // model_glm_bernoulli.train(&flower_x_train, &flower_y_train)?;

    // // Creating some dummy test data.
    // let test_matrix = Matrix::ones(1, 4);
    // let _ = model_glm_bernoulli.predict(&test_matrix)?;

    // // predict
    // let predictions = model_glm_bernoulli.predict(&flower_x_test)?;
    // let predictions = predictions.into_vec();

    // // Score how well we did
    // let mut correct_hits = 0;
    // let mut total_hits = 0;
    // for (&predicted, actual) in predictions.iter().zip(flower_y_test) {
    //     if predicted == actual {
    //         correct_hits += 1;
    //     }
    //     total_hits += 1;
    // }
    // println!("Naive Bayes Gaussian: accuracy: {:?}", correct_hits as f64/total_hits as f64); // accuracy is quite good.

    // Naive bayes bernoulli
    let mut model = NaiveBayes::<Bernoulli>::new();
    model.train(&flower_x_train, &flower_y_train_onehot)
        .expect("failed to train model of flowers");

    // // How many classes do I h ave?
    // println!("{:?}", model.class_prior());

    // Creating some dummy test data.
    let test_matrix = Matrix::ones(1, 4);
    let _ = model.predict(&test_matrix)?;

    // predict
    let predictions = model.predict(&flower_x_test)?;
    let predictions = predictions.into_vec();
    println!("{:?}", predictions);


    // Score how well we did
    let mut correct_hits = 0;
    let mut total_hits = 0;
    for (predicted, actual) in predictions.chunks(3).zip(flower_y_test_onehot.chunks(3)) {
        if predicted == actual {
            correct_hits += 1;
        }
        total_hits += 1;
    }
    println!("Naive Bayes Bernoulli: accuracy: {:?}", correct_hits as f64/total_hits as f64); // accuracy is quite good.

    // this does not work all the time.
    // let nb_bernoulli_acc = accuracy(predictions.iter(), flower_y_test_onehot.iter());
    // println!("{:?}", nb_bernoulli_acc);

    // // Neural Network

    // // Set the layer sizes - from input to output
    // // let layers = &[input_feature_dim, whatever layers you want, output_feature_dimension]
    // // let layers = &[4,5,11,7,3];
    // let layers = &[4,11,3];

    // // Choose the BCE criterion with L2 regularization (`lambda=0.1`).
    // let criterion = BCECriterion::new(Regularization::L2(0.1));

    // // We will just use the default stochastic gradient descent.
    // let mut model = NeuralNet::new(layers, criterion, StochasticGD::default());
    // model.train(&flower_x_train, &flower_y_train).unwrap();

    // // Creating some dummy test data.
    // let test_matrix = Matrix::ones(1, 4);
    // let _ = model.predict(&test_matrix)
    //     .expect("Failed to predict");

    // // predict
    // let predictions = model.predict(&flower_x_test).unwrap();
    // let predictions = predictions.into_vec();

    // // Score how well we did
    // let mut correct_hits = 0;
    // let mut total_hits = 0;
    // for (predicted, actual) in predictions.chunks(3).zip(flower_y_test.chunks(3)) {
    //     if predicted == actual {
    //         correct_hits += 1;
    //     }
    //     total_hits += 1;
    // }
    // println!("Neural Network: accuracy: {:?}", correct_hits as f64/total_hits as f64); // accuracy is quite good.

    Ok(())
}