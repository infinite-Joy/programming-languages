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

#[derive(Debug)]
enum CliError {
    IoError(io::Error),
    ParseError(num::ParseIntError),
}

impl From<io::Error> for CliError {
    fn from(error: io::Error) -> Self {
        CliError::IoError(error)
    }
}

impl From<num::ParseIntError> for CliError {
    fn from(error: num::ParseIntError) -> Self {
        CliError::ParseError(error)
    }
}

// fn smart_open(file_name: &str) -> Result<i32, CliError> {
//     let mut file = std::fs::File::open("/Users/joydeep/thinking/programming-languages/rust-lang/smart-open/foo.txt")?;
//     let mut contents = String::new();
//     file.read_to_string(&mut contents)?;
//     let num: i32 = contents.trim().parse()?;
//     Ok(num)
// }

// pub fn smart_open(filepath: &str) -> String {
// pub fn smart_open() -> std::io::Result<String> {
pub fn smart_open(filepath: &str) -> std::io::Result<String> {
// pub fn smart_open() -> Result<i32,Box<Error>> {
// fn smart_open() -> std::io::Result<()> {
    
    // let filepath_string = String::from(filepath);
    // let from_string = Path::new(&filepath_string);
    // let file = File::open("/Users/joydeep/thinking/programming-languages/rust-lang/smart-open/foo.txt")
    let file = File::open(filepath)
        .expect("Unable to open the file");
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents)
        .expect("Unable to read the file");
    Ok(contents.trim().to_string())
    // Ok(contents)
    // Ok(())
    // let mut d = GzDecoder::new(filepath.as_bytes());
    // let mut s = String::new();
    // d.read_to_string(&mut s).unwrap();
    // s
}