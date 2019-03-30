/// Data gathered from https://www.kaggle.com/vikrishnan/boston-house-prices
/// Boston dataset: https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html
/// This module shows how to run regression models
extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;

use std::io::prelude::*;
use std::io::BufReader;
use std::path::Path;
use std::fs::File;
use std::vec::Vec;
use std::error::Error;

use rusty_machine;
use rusty_machine::linalg::Matrix;
use rusty_machine::linalg::BaseMatrix;
use rusty_machine::linalg::Vector;
use rusty_machine::learning::lin_reg::LinRegressor;
use rusty_machine::learning::gp::GaussianProcess;
use rusty_machine::learning::gp::ConstMean;
use rusty_machine::learning::toolkit::kernel;
use rusty_machine::learning::glm::{GenLinearModel, Normal};
use rusty_machine::analysis::score::neg_mean_squared_error;
use rusty_machine::learning::SupModel;

// use ndarray::{Array, arr1};
use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;

#[derive(Debug, Deserialize)]
struct BostonHousing {
    crim: f64, // per capita crime rate by town
    zn: f64, // proportion of residential land zoned for lots over 25,000 sq.ft.
    indus: f64, // proportion of non-retail business acres per town.
    chas: f64, // Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
    nox: f64, // nitrogen oxides concentration (parts per 10 million).
    rm: f64, // average number of rooms per dwelling.
    age: f64, // proportion of owner-occupied units built prior to 1940.
    dis: f64, // weighted mean of distances to five Boston employment centres.
    rad: f64, // index of accessibility to radial highways.
    tax: f64, // full-value property-tax rate per $10,000.
    ptratio: f64, // pupil-teacher ratio by town.
    black: f64, // 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.
    lstat: f64, // lower status of the population (percent).
    medv: f64, // median value of owner-occupied homes in $1000s.
}

impl BostonHousing {
    fn new(v: Vec<&str>) -> BostonHousing {
        let f64_formatted: Vec<f64> = v.iter().map(|s| s.parse().unwrap()).collect();
        BostonHousing { crim: f64_formatted[0], zn: f64_formatted[1], indus: f64_formatted[2], chas: f64_formatted[3],
                        nox: f64_formatted[4], rm: f64_formatted[5], age: f64_formatted[6], dis: f64_formatted[7],
                        rad: f64_formatted[8], tax: f64_formatted[9], ptratio: f64_formatted[10], black: f64_formatted[11],
                        lstat: f64_formatted[12], medv: f64_formatted[13] }
    }

    fn into_feature_vector(&self) -> Vec<f64> {
        vec![self.crim, self.zn, self.indus, self.chas, self.nox,
             self.rm, self.age, self.dis, self.rad,
             self.tax, self.ptratio, self.black, self.lstat]
    }

    fn into_labels(&self) -> f64 {
        self.medv
    }
}

fn get_boston_record(s: String) -> BostonHousing {
    let v: Vec<&str> = s.split_whitespace().collect();
    let b: BostonHousing = BostonHousing::new(v);
    b
}

fn get_boston_records_from_file(filename: impl AsRef<Path>) -> Vec<BostonHousing> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines().enumerate()
        .map(|(n, l)| l.expect(&format!("Could not parse line no {}", n)))
        .map(|r| get_boston_record(r))
        .collect()
}

fn r_squared_score(y_test: &Vec<f64>, y_preds: &Vec<f64>) -> f64 {
    let model_variance: f64 = y_test.iter().zip(y_preds.iter()).fold(
        0., |v, (y_i, y_i_hat)| {
            v + (y_i - y_i_hat).powi(2)
        }
    );

    // get the mean for the actual values to be used later
    let y_test_mean = y_test.iter().sum::<f64>() as f64
        / y_test.len() as f64;

    // finding the variance
    let variance =  y_test.iter().fold(
        0., |v, &x| {v + (x - y_test_mean).powi(2)}
    );
    let r2_calculated: f64 = 1.0 - (model_variance / variance);
    r2_calculated
}

fn main() -> Result<(), Box<Error>> {
    // Get all the data
    let filename = "data/housing.csv";
    let mut data = get_boston_records_from_file(&filename);

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
    let boston_x_train: Vec<f64> = train_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let boston_y_train: Vec<f64> = train_data.iter().map(|r| r.into_labels()).collect();

    let boston_x_test: Vec<f64> = test_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let boston_y_test: Vec<f64> = test_data.iter().map(|r| r.into_labels()).collect();

    // using ndarray
    // let boston_x_train = Array::from_shape_vec((train_size, 13), boston_x_train).unwrap();
    // let boston_y_train = Array::from_vec(boston_y_train);
    // let boston_x_test = Array::from_shape_vec((test_size, 13), boston_x_test).unwrap();
    // let boston_y_test = Array::from_vec(boston_y_test);

    // COnvert the data into matrices for rusty machine
    let boston_x_train = Matrix::new(train_size, 13, boston_x_train);
    let boston_y_train = Vector::new(boston_y_train);
    let boston_x_test = Matrix::new(test_size, 13, boston_x_test);
    // let boston_y_test = Vector::new(boston_y_test);
    let boston_y_test = Matrix::new(test_size, 1, boston_y_test);

    // Create a linear regression model
    let mut lin_model = LinRegressor::default();
    println!("{:?}", lin_model);

    // Train the model
    lin_model.train_with_optimization(&boston_x_train, &boston_y_train);

    // Now we will predict
    let predictions = lin_model.predict(&boston_x_test).unwrap();
    let predictions = Matrix::new(test_size, 1, predictions);
    let acc = neg_mean_squared_error(&predictions, &boston_y_test);
    println!("linear regression error: {:?}", acc);
    println!("linear regression R2 score: {:?}", r_squared_score(
        &boston_y_test.data(), &predictions.data()));

    // Create a gaussian process regression
    // A squared exponential kernel with lengthscale 2 and amplitude 1
    let ker = kernel::SquaredExp::new(2., 1.);

    // zero function as mean function
    let zero_mean = ConstMean::default();

    // defining the model with noise 10
    let mut gaus_model = GaussianProcess::new(ker, zero_mean, 10f64);

    gaus_model.train(&boston_x_train, &boston_y_train)?;

    let predictions = gaus_model.predict(&boston_x_test).unwrap();
    let predictions = Matrix::new(test_size, 1, predictions);
    let acc = neg_mean_squared_error(&predictions, &boston_y_test);
    println!("gaussian process regression error: {:?}", acc);
    println!("gaussian process regression R2 score: {:?}", r_squared_score(
        &boston_y_test.data(), &predictions.data()));

    // Create a poisson generalised linear mode
    let mut poisson_glm_model = GenLinearModel::new(Normal);
    poisson_glm_model.train(&boston_x_train, &boston_y_train)?;

    let predictions = poisson_glm_model.predict(&boston_x_test).unwrap();
    let predictions = Matrix::new(test_size, 1, predictions);
    let acc = neg_mean_squared_error(&predictions, &boston_y_test);
    println!("glm poisson accuracy: {:?}", acc);
    println!("glm poisson R2 score: {:?}", r_squared_score(
        &boston_y_test.data(), &predictions.data()));

    Ok(())
}