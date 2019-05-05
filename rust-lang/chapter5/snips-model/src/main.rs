#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;
#[macro_use] extern crate serde_derive;
extern crate snips_nlu_lib;

#[cfg(test)] mod tests;

use std::sync::Mutex;

use snips_nlu_lib::SnipsNluEngine;
use rocket::{Rocket, State};
use rocket_contrib::json::Json;

type Engine = Mutex<SnipsNluEngine>;

#[derive(Serialize, Deserialize)]
struct Message {
    contents: String
}

fn init_engine() -> SnipsNluEngine {
    let engine_dir = "/home/saionee/opensource/programming-languages/rust-lang/chapter5/snips-nlu-rs/snips.model2";
    let top_intents = true;

    println!("\nLoading the nlu engine...");
    let engine = SnipsNluEngine::from_path(engine_dir).unwrap();
    engine
}

#[get("/")]
fn hello() -> &'static str {
    "Hello, world!"
}

#[post("/infer", format = "json", data = "<message>")]
fn infer(message: Json<Message>, engine: State<Engine>) -> String {
    let engine = engine.lock().unwrap();
    let result = engine.get_intents(query.trim()).unwrap();
    let result_json = serde_json::to_string_pretty(&result).unwrap();
    result_json

}


fn rocket() -> Rocket {
    // Initialize the `entries` table in the in-memory database.
    let engine = init_engine();

    // Have Rocket manage the database pool.
    rocket::ignite()
        .manage(Mutex::new(engine))
        .mount("/", routes![hello, infer])
}

fn main() {
    rocket().launch();
}
