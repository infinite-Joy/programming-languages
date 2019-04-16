#[macro_use]
extern crate serde_derive;

use std::fs::File;
use std::io::Read;

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Person {
    first_name: String,
    last_name: String,
    age: u8,
    address: Address,
    phone_numbers: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Prizes {
    prizes: Vec<Prize>,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
struct Prize {
    category: String,
    // add more
}

fn main() {
    let the_file = r#"{
        "FirstName": "John",
        "LastName": "Doe",
        "Age": 43,
        "Address": {
            "Street": "Downing Street 10",
            "City": "London",
            "Country": "Great Britain"
        },
        "PhoneNumbers": [
            "+44 1234567",
            "+44 2345678"
        ]
    }"#;
    // let mut file = File::open("data/prize.json")
    //     .expect("file should open read only");
    // let person: Person = serde_json::from_reader(file)
    //     .expect("file should be proper JSON");

    // in case i dont know the values of the file.
    let person: serde_json::Value = serde_json::from_str(the_file).expect("JSON was not well-formatted");
    let address = person.get("Address").unwrap();
    println!("{:?}", address.get("City").unwrap());

    // this is great but I am not leveraging the strongly types ability of RUst.
    // using strongly typed data structures is great because you want the program to fail
    // when the data format has changed. which they do a lot. and you want the information
    // fast.

    let mut file = File::open("data/prize.json")
        .expect("file should open read only");
    let person: Prize = serde_json::from_reader(file)
        .expect("file should be proper JSON");


}