#[macro_use]
extern crate serde_derive;
#[macro_use]
extern crate lambda_runtime;
extern crate regex;
use std::collections;
use std::collections::hash_map::Entry::{Occupied, Vacant};
#[macro_use]
extern crate serde_json;
use std::io;
use std::io::prelude::*;

use lambda_runtime::error::HandlerError;
use regex::Regex;


#[derive(Deserialize, Clone)]
struct CustomEvent {
    string: String,
}

#[derive(Serialize, Clone)]
struct CustomOutput {
    message: String,
}

fn main() {
    lambda!(my_handler);

    //let mut map = collections::HashMap::<String, u32>::new();
    //let re = Regex::new(r"\w+").unwrap();
    //let sample_text = "This is me me.";
    //for caps in re.captures_iter(&sample_text) {
    //    if let Some(cap) = caps.get(0) {
    //        let word = cap.as_str();
    //        match map.entry(word.to_string()) {
    //            Occupied(mut view) => { *view.get_mut() += 1; }
    //            Vacant(view) => { view.insert(1); }
    //        }
    //    }
    //}
    //// Write counts
    //let mut words: Vec<&String> = map.keys().collect();
    //words.sort();
    //for &word in &words {
    //    if let Some(count) = map.get(word) {
    //        println!("{}\t{}", count, word);
    //    }
    //}

    //// Serialize it to a JSON string.
    //let j = serde_json::to_string(&map).unwrap();

    //// Print, write to a file, or send to an HTTP server.
    //println!("{}", j);
}

fn my_handler(e: CustomEvent, ctx: lambda_runtime::Context) -> Result<CustomOutput, HandlerError> {
    let mut map = collections::HashMap::<String, u32>::new();
    let re = Regex::new(r"\w+").unwrap();
    if e.string == "" {
        return Err(ctx.new_error("Missing input string!"));
    }
    for caps in re.captures_iter(&e.string) {
        if let Some(cap) = caps.get(0) {
            let word = cap.as_str();
            match map.entry(word.to_string()) {
                Occupied(mut view) => { *view.get_mut() += 1; }
                Vacant(view) => { view.insert(1); }
            }
        }
    }

    // Serialize it to a JSON string.
    let j = serde_json::to_string(&map).unwrap();

    Ok(CustomOutput{
        message: format!("{}", j),
    })
}
