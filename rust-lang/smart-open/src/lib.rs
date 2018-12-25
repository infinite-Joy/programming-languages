extern crate flate2;

use std::io::prelude::*;
use std::fs::File;
use std::io::BufReader;
use std::path::Path;
use std::ffi::OsStr;
use std::string::String;
use std::error::Error;
use flate2::read::GzDecoder;

use std::io::{self, Read};
use std::num;

pub fn smart_open(filepath: &str) -> std::io::Result<String> {
    let file = File::open(filepath)
        .expect("Unable to open the file");
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents)
        .expect("Unable to read the file");
    Ok(contents.trim().to_string())
}