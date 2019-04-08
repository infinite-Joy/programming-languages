use std::vec::Vec;
use std::collections::HashSet;
// use std::io::Error;
use std::error::Error;
use std::cmp::Ordering;
use std::iter::FromIterator;

use rand;
use rand::distributions::{Bernoulli, Distribution};
use itertools;
use itertools::iproduct;
use itertools::Itertools;
use ndarray;
use ndarray::{arr2, Array, ArrayBase, OwnedRepr, Dim, Axis};
use ndarray::prelude::*;

pub fn r_squared_score(y_test: &Vec<f64>, y_preds: &Vec<f64>) -> f64 {
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