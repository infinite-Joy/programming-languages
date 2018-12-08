extern crate csv;
#[macro_use]
extern crate serde_derive;
#[macro_use]
extern crate ndarray;

use std::error::Error;
use csv::ReaderBuilder;
use std::process;
use std::fs::File;
use std::env;
use std::ffi::OsString;
use ndarray::prelude::*;
use ndarray::{arr1, arr2, Array1, ArrayView1, Array2, Axis};
use ndarray::Dimension;
use ndarray::StrideShape;
use ndarray::Dim;

#[derive(Debug)]
#[derive(Deserialize)]
struct IrisRecord {
    sepal_length: f64,
    sepal_width: f64,
    petal_length: f64,
    petal_width: f64,
    species: String,
}

/// Returns the first positional argument sent to this process. If there are no
/// positional arguments, then this returns an error.
fn get_first_arg() -> Result<OsString, Box<Error>> {
    match env::args_os().nth(1) {
        None => Err(From::from("expected 1 argument, but got none")),
        Some(file_path) => Ok(file_path),
    }
}

fn example() -> Result<(), Box<Error>> {
    println!("first try using simple csv");
    let file_path = get_first_arg()?;
    let file = File::open(file_path)?;
    let mut rdr = ReaderBuilder::new()
        .has_headers(false)
        .from_reader(file);
    //let mut iris_matrix: Vec<IrisRecord> = vec![];
    //let mut iris_matrix: Vec<Vec<f64>> = vec![];
    let mut iris_matrix: Vec<f64> = vec![];
    //{
    //    let headers = rdr.headers()?;
    //    assert_eq!(headers, vec!["Boston", "United States", "4628910"]);
    //}

    for result in rdr.deserialize() {
    //for result in rdr.records() {
        let record: IrisRecord = result?;
        //let record = result?;
        //let sepal_length = record[0] as f64;
        //let sepal_width = record[1] as f64;
        //let petal_length = record[2] as f64;
        //let petal_width = record[3] as f64;
        //let species = &record[4];
        //println!(
        //    "{:?}, {:?}, {:?}, {:?}, {:?}",
        //    record.sepal_length, record.sepal_width, record.petal_length, record.petal_width, record.species
        //    );
        // adding all of them in a flat vector. will convert to ndarray and then reshape.
        iris_matrix.push(record.sepal_length);
        iris_matrix.push(record.sepal_width);
        iris_matrix.push(record.petal_length);
        iris_matrix.push(record.petal_width);
    }
    //println!("{:#?}", iris_matrix);
    // passing variables as dimension is not working. Need to take a look.
    let ndim = 4;
    let n_samples = (iris_matrix.len() as i32)/ndim;
    println!("{:#?}", n_samples);
    let iris_ndmatrix = Array::from_shape_vec((150, 4), iris_matrix);
    let trm = iris_ndmatrix.t();
    println!("{:#?}", iris_ndmatrix);
    //println!("Shape of the matrix {:?}", iris_ndmatrix.dim());
    //iris_ndmatrix.invert_axis(Axis(0));
    //println!("Shape of the matrix after transposition {:?}", &iris_ndmatrix.shape());
    Ok(())
}

pub fn main() {
    if let Err(err) = example() {
        println!("{}", err);
        process::exit(1);
    }
}
