use std::fs::File;
use std::io::BufReader;
use std::result::Result;
use std::error::Error;

use serde_xml_rs;
use serde_xml_rs::from_reader;
use serde_xml_rs::Deserializer;

#[derive(Deserialize, Debug)]
struct Project {
    name: String,
    libraries: Vec<Libraries>
}

#[derive(Deserialize, Debug)]
struct Libraries {
    libraries: Vec<Library>,
}

#[derive(Deserialize, Debug)]
struct Library {
    #[serde(rename = "groupId")]
    group_id: String,
    #[serde(rename = "artifactId")]
    artifact_id: String,
    version: String,
}

pub fn run() -> Result<(), Box<Error>> {
    let file = File::open("data/sample_1.xml").unwrap();
    let project: Project = from_reader(file).unwrap();
    println!("{:#?}", project);
    Ok(())
}