extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;

use crfsuite::{Model, Attribute, CrfError};
use crfsuite::{Trainer, Algorithm, GraphicalModel};

// data from here https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus

use std::io;
use std::vec::Vec;
use std::error::Error;
use std::io::Write;
use std::fs::File;

use csv;
use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;

use stopwords;
use std::collections::HashSet;
use stopwords::{Spark, Language, Stopwords};
use itertools::Itertools;
use vtext::tokenize::VTextTokenizer;
use rust_stemmers::{Algorithm as rs_algorithm, Stemmer};

const TRAIN_FILE: &str = "data.train";
const TEST_FILE: &str = "data.test";
const MODEL: &str = "model.bin";

#[derive(Debug, Deserialize)]
pub struct NER {
    #[serde(rename = "")]
    id: String,
    lemma: String,
    #[serde(rename = "next-lemma")]
    next_lemma: String,
    // next-next-lemma: String,
    // next-next-pos: String,
    // next-next-shape: String,
    // next-next-word: String,
    // next-pos: String,
    // next-shape: String,
    // next-word: String,
    // pos: String,
    // prev-iob: String,
    // prev-lemma: String,
    // prev-pos: String,
    // prev-prev-iob: String,
    // prev-prev-lemma: String,
    // prev-prev-pos: String,
    // prev-prev-shape: String,
    // prev-prev-word: String,
    // prev-shape: String,
    // prev-word: String,
    // sentence_idx: String,
    // shape: String,
    word: String,
    tag: String
}


fn main() -> Result<(), Box<Error>> {
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut data = Vec::new();
    for result in rdr.deserialize() {
        let r: NER = result?;
        data.push(r);
    }
    println!("{:?}", data.len());
    data.shuffle(&mut thread_rng());

    // separate out to train and test datasets.
    let test_size: f32 = 0.2;
    let test_size: f32 = data.len() as f32 * test_size;
    let test_size = test_size.round() as usize;

    let (test_data, train_data) = data.split_at(test_size);


    let mut xseq_train = vec![];
    let mut yseq_train = vec![];
    for item in train_data {
        let seq = vec![Attribute::new(item.lemma.clone(), 1.0), Attribute::new(item.next_lemma.clone(), 0.5)]; // higher weightage for the mainword.
        xseq_train.push(seq);
        yseq_train.push(item.tag.clone());
    }

    let mut xseq_test = vec![];
    let mut yseq_test = vec![];
    for item in test_data {
        let seq = vec![Attribute::new(item.lemma.clone(), 1.0), Attribute::new(item.next_lemma.clone(), 0.5)]; // higher weightage for the mainword.
        xseq_test.push(seq);
        yseq_test.push(item.tag.clone());
    }

    let mut trainer = Trainer::new(true);
    trainer.select(Algorithm::LBFGS, GraphicalModel::CRF1D).unwrap();
    trainer.append(&xseq_train, &yseq_train, 0i32).unwrap();
    trainer.train("test.crfsuite", -1i32).unwrap();
    drop(trainer);

    // evaluation
    let model = Model::from_file("test.crfsuite").unwrap();
    let mut tagger = model.tagger().unwrap();
    let preds = tagger.tag(&xseq_test).unwrap();
    println!("{:?}", preds.len());

    // accuracy
    let mut hits = 0;
    let mut correct_hits = 0;
    let preds_clone = preds.clone();
    for (predicted, actual) in preds.iter().zip(yseq_test) {
        if predicted.clone() == actual {
            correct_hits += 1;
        }
        hits += 1;
    }
    assert_eq!(hits, preds_clone.len());
    println!("accuracy={} ({}/{} correct)", correct_hits as f32 / hits as f32, correct_hits, preds_clone.len());

    Ok(())
}
