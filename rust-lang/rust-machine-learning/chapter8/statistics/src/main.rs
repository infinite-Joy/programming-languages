#![allow(non_snake_case)]

use std::path::Path;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

// https://nbviewer.jupyter.org/urls/umich.box.com/shared/static/7kh8amlez7bx3qlqa6aa.ipynb?create=1

fn process_gene_expresssion_data(thisline: &String, SIF: &HashMap<String, String>) {
    println!(" this line: {:?}", thisline);
    let SID: Vec<String> = thisline.split("\t").map(|s| s.to_owned()).collect();
    println!(" sid: {:?}", SID);
    let indices = SID.iter()
                .enumerate()
                .filter(|&(_, x)| x.starts_with("GSM") )
                .map(|(i, _)| i);
    let SID = indices.map(|i| SID[i].clone());
    let STP: Vec<String> = SID.map(
        |k| SIF.get(&k.to_string()).unwrap())
        .cloned().collect();
    println!(" STP: {:?}", STP);
}


fn process_file(filename: &Path) -> io::Result<HashMap<String, String>> {
    let mut SIF = HashMap::new();
    let file = File::open(filename).unwrap();
    let mut subset_description = String::new();
    let mut after_dataset_table_begin = false;
    for line in BufReader::new(file).lines() {
        let thisline = line?;
        let line_split: Vec<String> = thisline.split("=").map(|s| s.to_owned()).collect();
        println!("this line: {:?}", thisline);
        if thisline.starts_with("!dataset_table_begin") {
            after_dataset_table_begin = true;
        }
        if after_dataset_table_begin {
            process_gene_expresssion_data(&thisline, &SIF);

        } else {
            if thisline.starts_with("!subset_description") {
                subset_description = line_split[1].trim().to_owned();
            };
            println!("subset description {:?}", subset_description);
            let subset_ids = if thisline.starts_with("!subset_sample_id") {
                let subset_ids = line_split[1].split(",");
                let subset_ids = subset_ids.map(|s| s.trim().to_owned());
                subset_ids.collect()
            } else {
                Vec::new()
            };
            println!("subset ids {:?}", subset_ids);
            for k in subset_ids {
                SIF.insert(k, subset_description.to_owned());
                println!("SIF: {:?}", SIF);
            }
        }
    }
    Ok(SIF)
}

fn main() {
    let filename = Path::new("GDS1615_full.soft");
    process_file(&filename).unwrap();
}
