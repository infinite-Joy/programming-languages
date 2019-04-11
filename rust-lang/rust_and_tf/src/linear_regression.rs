#![allow(non_snake_case)]

use std::error::Error;
use std::result::Result;
use std::io::prelude::*;
use std::io::BufReader;
use std::path::Path;
use std::fs::File;
use std::vec::Vec;

use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;
use transpose;

use tensorflow as tf;
use tf::expr::{Compiler, Constant};
use tf::{Graph, Tensor, DataType};
use tf::{Session, SessionOptions, SessionRunArgs};

#[cfg_attr(feature="examples_system_alloc", global_allocator)]
#[cfg(feature="examples_system_alloc")]
static ALLOCATOR: std::alloc::System = std::alloc::System;

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

pub fn run() -> Result<(), Box<dyn Error>> {
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

    // println!("{:?}", boston_y_train.len());
    println!("{:?}", boston_x_train.len());


    // Define graph.
    let mut graph = Graph::new();
    let dim = (405, 13);
    // let X = <Tensor<f64>>::new(&[dim.0, dim.1]).with_values(&boston_x_train)?;
    // let y = <Tensor<f64>>::new(&[dim.0, 1]).with_values(&boston_y_train)?;
    let X = <Tensor<f64>>::new(&[2, 2]).with_values(&[1.0, 2.0, 3.0, 4.0])?;
    let y = <Tensor<f64>>::new(&[2, 1]).with_values(&[2.0, 4.0])?;
    
    let X_const = {
        let mut c = graph.new_operation("Const", "X")?;
        c.set_attr_tensor("value", X)?;
        c.set_attr_type("dtype", DataType::Double)?; // check the enums https://github.com/tensorflow/rust/blob/ddff61850be1c8044ac86350caeed5a55824ebe4/src/lib.rs#L297
        c.finish()?
    };
    let y_const = {
        let mut c = graph.new_operation("Const", "y")?;
        c.set_attr_tensor("value", y)?;
        c.set_attr_type("dtype", DataType::Double)?;
        c.finish()?
    };
    let XT = {
        let mut op = graph.new_operation("Transpose", "x_t")?;
        op.add_input(X_const);
        op.add_input(2);
        op.finish()?
    };
    // let XT = {
    //     let mut op = graph.new_operation("MatMul", "mul")?;
    //     op.add_input(X_const);
    //     op.add_input(y_const);
    //     op.finish()?
    // };
    // let inverse = {
    //     let mut op = graph.new_operation("MatrixInverse", "x_inv")?;
    //     op.add_input(XT);
    //     op.finish()?
    // };

    // Run graph.
    let session = Session::new(&SessionOptions::new(), &graph)?;
    let mut args = SessionRunArgs::new();
    // let inverse_token = args.request_fetch(&inverse, 0);
    let inverse_token = args.request_fetch(&XT, 0);
    session.run(&mut args)?;
    let inverse_token_res: Tensor<f64> = args.fetch::<f64>(inverse_token)?;
    println!("Now the inverse", );
    println!("{:?}", &inverse_token_res[..]);

    Ok(())
}