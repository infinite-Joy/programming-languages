extern crate simple_logger;

use serde_derive;
use serde_derive::{Serialize, Deserialize};
use lambda_runtime;
use lambda_runtime::{lambda, Context, error::HandlerError};
use log;
use log::error;
use std::error::Error;
use std::collections;
use std::collections::hash_map::Entry::{Occupied, Vacant};
use regex;
use regex::Regex;
use simple_error::bail;

use csv::ReaderBuilder;
use xgboost;
use xgboost::{parameters, DMatrix, Booster};

use ml_utils::datasets::Flower;

fn flower_decoder(item: f32) -> String {
    match item as i32 {
        0 => "setosa".to_string(),
        1 => "versicolor".to_string(),
        2 => "virginica".to_string(),
        l => panic!("Not able to parse the target. Some other target got passed. {:?}", l),
    }
}

fn predict(data: &String) -> Result<String, Box<dyn Error>> {
    println!("Loading model");
    let booster = Booster::load("xgb.model")?;
    let mut rdr = ReaderBuilder::new()
        .delimiter(b',')
        .from_reader(data.as_bytes());
    let mut data = Vec::new();
    for result in rdr.deserialize() {
        let r: Flower = result.unwrap();
        data.push(r); // data contains all the records
    }
    let val_size: usize = data.len();

    // differentiate the features and the labels.
    let flower_x_val: Vec<f32> = data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_val: Vec<f32> = data.iter().map(|r| r.into_labels()).collect();

    // validation matrix with 1 row
    let mut dval = DMatrix::from_dense(&flower_x_val, val_size).unwrap();
    dval.set_labels(&flower_y_val).unwrap();

    let preds = booster.predict(&dval).unwrap();
    Ok(flower_decoder(preds[0]))
}

#[derive(Serialize, Deserialize)]
struct CustomEvent {
    string: String,
}

fn main() -> Result<(), Box<dyn Error>> {
    simple_logger::init_with_level(log::Level::Debug).unwrap();
    lambda!(my_handler);

    Ok(())
}

fn my_handler(event: CustomEvent, ctx: Context) -> Result<String, HandlerError> {
    if event.string == "" {
        error!("Empty name in request {}", ctx.aws_request_id);
        bail!("Empty name");
    }
    // let mut map = collections::HashMap::<String, u32>::new();
    // let re = Regex::new(r"\w+").unwrap();
    // for caps in re.captures_iter(&event.string) {
    //     if let Some(cap) = caps.get(0) {
    //         let word = cap.as_str();
    //         match map.entry(word.to_string()) {
    //             Occupied(mut view) => { *view.get_mut() += 1; }
    //             Vacant(view) => { view.insert(1); }
    //         }
    //     }
    // }
    let prediction = match predict(&event.string) {
        Ok(p) => p,
        Err(_) => "Not able to get the prediction".to_string(),
    };

    // Serialise to a json string
    // let j = serde_json::to_string(&map).unwrap();

    Ok(prediction)
    // Ok(j)
}


#[cfg(test)]
mod tests {
    use super::*;
    use csv;
    use std::io;


    // #[test]
    // fn test_predict() {
    //     let data = "sepal_length,sepal_width,petal_length,petal_width,species\n5.1,3.5,1.4,0.2,setosa\n";
    //     let mut rdr = csv::Reader::from_reader(data.as_bytes());
    //     let mut data = Vec::new();
    //     for result in rdr.deserialize() {
    //         let r: Flower = result.unwrap();
    //         data.push(r); // data contains all the records
    //     }
    //     assert_eq!(data[0].sepal_length, 5.1);
    // }
    #[test]
    fn test_predict() {
        let data = "sepal_length,sepal_width,petal_length,petal_width,species\n5.1,3.5,1.4,0.2,setosa\n";
        let res = predict(&data.to_string());
        assert_eq!(res.unwrap(), "setosa".to_string());
    }
}