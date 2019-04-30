extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;

use std::io;
use std::vec::Vec;
use std::error::Error;

use csv;
use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;

use fasttext::FastText;
use fasttext::Args;
use fasttext::Prediction;
use fasttext::{ModelName, LossName};

#[derive(Debug, Deserialize)]
pub struct SpookyAuthor {
    id: String,
    text: String,
    author: String
}

impl SpookyAuthor {
    fn into_labels(&self) -> String {
        match self.author.as_str() {
            "EAP" => String::from("__label__EAP"),
            "HPL" => String::from("__label__HPL"),
            "MWS" => String::from("__label__MWS"),
            l => panic!("Not able to parse the target. Some other target got passed. {:?}", l),
        }
    }

    pub fn into_training_string(&self) -> String {
        [self.into_labels(), self.text.clone()].join(" ")
    }
}

fn create_training_file(filename: &str) {
    unimplemented!()
}

fn main() {


    // let mut args = Args::new();
    // // args.set_input("data/train.csv");
    // args.set_input("cooking.train");
    // args.set_output("output.model");
    // args.set_model(ModelName::SUP);
    // args.set_loss(LossName::SOFTMAX);
    // println!("{:?}", args);
    // let mut ft_model = FastText::new();
    // ft_model.train(&args).unwrap();
    // let preds = ft_model.predict("I am going to the end of the world", 2, 0.000000001).unwrap();
    // println!("{:?}", preds);
}