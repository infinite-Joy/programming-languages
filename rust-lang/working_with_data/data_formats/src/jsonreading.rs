use std::str::FromStr;
use serde::{de, Deserialize, Deserializer};
use std::result::Result;
use std::vec::Vec;
use std::error::Error;
use std::fs::File;

#[derive(Debug, Serialize, Deserialize)]
// #[serde(rename_all = "PascalCase")]
struct Prizes {
    prizes: Vec<Prize>,
}

#[derive(Debug, Serialize, Deserialize)]
#[allow(non_snake_case)]
struct Prize {
    category: String,
    #[serde(default)]
    overallMotivation: Option<String>,
    laureates: Vec<NobelLaureates>,
    #[serde(deserialize_with = "de_u16_from_str")]
    year: u16,
}

#[derive(Debug, Serialize, Deserialize)]
// #[serde(rename_all = "PascalCase")]
struct NobelLaureates {
    share: String,
    #[serde(default)]
    motivation: Option<String>,
    surname: String,
    #[serde(deserialize_with = "de_u16_from_str")]
    id: u16,
    firstname: String,
}

fn de_u16_from_str<'de, D>(deserializer: D) -> Result<u16, D::Error>
    where D: Deserializer<'de>
{
    let s = String::deserialize(deserializer)?;
    u16::from_str(&s).map_err(de::Error::custom)
}

pub fn run() -> Result<(), Box<Error>> {
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
    // in case i dont know the values of the file.
    let person: serde_json::Value = serde_json::from_str(the_file).expect("JSON was not well-formatted");
    let address = person.get("Address").unwrap();
    println!("{:?}", address.get("City").unwrap());

    // this is great but I am not leveraging the strongly types ability of RUst.
    // using strongly typed data structures is great because you want the program to fail
    // when the data format has changed. which they do a lot. and you want the information
    // fast.

    // reference https://github.com/serde-rs/json/issues/317

    println!("from prizes json file", );

    let file = File::open("data/prize.json")
        .expect("file should open read only");
    let prizes_data: Prizes = serde_json::from_reader(file)
        .expect("file should be proper JSON");
    let prizes_0 = &prizes_data.prizes[0];
    println!("category: {:?}", prizes_0.category);
    println!("laureates: {:?}", prizes_0.laureates);
    println!("overall motivation: {:?}", prizes_0.overallMotivation);
    println!("year: {:?}", prizes_0.year);

    Ok(())
}