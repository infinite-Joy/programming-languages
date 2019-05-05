
#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;
#[macro_use] extern crate serde_derive;
extern crate snips_nlu_lib;

#[cfg(test)] mod tests;

use std::sync::Mutex;
use std::collections::HashMap;

use snips_nlu_lib::SnipsNluEngine;

use rocket::State;
use rocket_contrib::json::{Json, JsonValue};

#[derive(Serialize, Deserialize)]
struct Message {
    contents: String
}

#[get("/")]
fn hello() -> &'static str {
    "Hello, world!"
}

#[post("/infer", format = "json", data = "<message>")]
fn infer(message: Json<Message>) -> String {
    let query = message.0.contents;
    let engine_dir = "/home/saionee/opensource/programming-languages/rust-lang/chapter5/snips-nlu-rs/snips.model";
    let top_intents = true;

    println!("\nLoading the nlu engine...");
    let engine = SnipsNluEngine::from_path(engine_dir).unwrap();

    // // query
    // let result_json = if top_intents {
    //     let result = engine.get_intents(query.trim()).unwrap();
    //     result
    //     // serde_json::to_string_pretty(&result).unwrap()
    // } else {
    //     let result = engine.parse(query.trim(), None, None).unwrap();
    //     result
    //     // serde_json::to_string_pretty(&result).unwrap()
    // };
    let result = engine.get_intents(query.trim()).unwrap();
    let result_json = serde_json::to_string_pretty(&result).unwrap();
    // println!("{}", result_json);
    // json!(result_json)
    result_json

}

fn main() {
    rocket::ignite().mount("/", routes![hello, infer]).launch();
}