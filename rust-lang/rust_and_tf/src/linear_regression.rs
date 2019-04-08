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
use tf::{Graph, Tensor};
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


    let mut g = Graph::new();
    Compiler::new(&mut g);
    let dim = (405, 13);
    let x = <Tensor<f64>>::new(&[dim.0, dim.1]).with_values(&boston_x_train).unwrap();
    let x_expr = <Constant<f64>>::new_expr(x.clone());

    let mut x_transpose = vec![0.0f64; boston_x_train.len()];
    // we dont have the functionality in rust tensorflow yet, hence we are using a different crate.
    transpose::transpose(
        &boston_x_train, &mut x_transpose, dim.1 as usize, dim.0 as usize);
    let xt_tensor = <Tensor<f64>>::new(&[dim.1, dim.0]).with_values(&x_transpose).unwrap();
    let xt_expr = <Constant<f64>>::new_expr(xt_tensor.clone());
    println!("{:?}", xt_tensor.dims());
    let theta = (xt_expr * x_expr) ;
    println!("{:?}", theta);


    // let (y_node, z_node) = {
    //     let mut compiler = Compiler::new(&mut g);
    //     let w = <Tensor<f32>>::new(&[1]).with_values(&[3.0_f32]).unwrap();
    //     let w_expr = <Constant<f32>>::new_expr(w);
    //     let x_expr = w_expr.clone() + 2.0f32;
    //     let y_expr = x_expr.clone() + 5.0f32;
    //     let z_expr = x_expr.clone() * 3.0f32;

    //     let y_node = compiler.compile(y_expr.clone())?;
    //     let z_node = compiler.compile(z_expr.clone())?;
    //     (y_node, z_node)
    // };

    // let options = SessionOptions::new();
    // let mut session = Session::new(&options, &g)?;

    // // Evaluate the graph.
    // let mut step = SessionRunArgs::new();
    // let output_token_y = step.request_fetch(&y_node, 0);
    // let output_token_z = step.request_fetch(&z_node, 0);
    // session.run(&mut step).unwrap();

    // // Check our results.
    // let output_tensor_y = step.fetch::<f32>(output_token_y)?;
    // let output_tensor_z = step.fetch::<f32>(output_token_z)?;
    // println!("constant evaluation: w = 3; x = w + 2; y = x + 5; z = x * 3");
    // println!("y => {:?}", output_tensor_y[0]);
    // println!("z => {:?}", output_tensor_z[0]);
    // session.close()?;

    Ok(())
}