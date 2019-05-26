#![allow(non_snake_case)]

use std::path::Path;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

// https://nbviewer.jupyter.org/urls/umich.box.com/shared/static/7kh8amlez7bx3qlqa6aa.ipynb?create=1

fn process_gene_expresssion_data_headers(thisline: &String, SIF: &HashMap<String, String>) -> (Vec<String>, Vec<String>, Vec<usize>) {
    println!(" this line: {:?}", thisline);
    let SID: Vec<String> = thisline.split("\t").map(|s| s.to_owned()).collect();
    let indices: Vec<usize> = SID.iter()
                .enumerate()
                .filter(|&(_, x)| x.starts_with("GSM") )
                .map(|(i, _)| i).collect();
    let SID: Vec<String> = indices.iter().map(|&i| SID[i].clone()).collect();
    println!(" sid: {:?}", SID);
    let STP: Vec<String> = SID.iter().map(
        |k| SIF.get(&k.to_string()).unwrap())
        .cloned().collect();
    println!(" STP: {:?}", STP);
    (SID, STP, indices)
}

/// Read the gene expression data as a list of lists, also get the gene identifiers
fn process_gene_expresssion_data(thisline: &String, indices: &Vec<usize>, SIF: &HashMap<String, String>) -> (Vec<String>, String) {
    let gene_expression_measure_values: Vec<String> = thisline.split("\t")
        .map(|s| s.to_owned()).collect();
    let gene_expression_measures: Vec<String> = indices.iter().map(|&i| gene_expression_measure_values[i].clone()).collect();
    let gene_identifiers = vec![gene_expression_measure_values[0].clone(), gene_expression_measure_values[1].clone()].join(";");
    (gene_expression_measures, gene_identifiers)
}


fn process_file(filename: &Path) -> io::Result<HashMap<String, String>> {
    let mut SIF = HashMap::new();
    let file = File::open(filename).unwrap();
    let mut subset_description = String::new();
    let mut within_dataset_table = false;
    let mut within_headers = true;
    let mut gene_expression_headers = true;
    let mut indices: Vec<usize> = Vec::new();
    'linereading: for line in BufReader::new(file).lines() {
        let thisline = line?;
        let line_split: Vec<String> = thisline.split("=").map(|s| s.to_owned()).collect();
        println!("this line: {:?}", thisline);
        if thisline.starts_with("!dataset_table_begin") {
            within_dataset_table = true;
            within_headers = false;
        }
        // let mut SID: Vec<String> = Vec::new();
        // let mut SID: Vec<String> = Vec::new();
        // let mut SID: Vec<usize> = Vec::new();
        if within_dataset_table && gene_expression_headers {
            let sid_stp_indices = process_gene_expresssion_data_headers(&thisline, &SIF);
            // SID, STP, indices = sid
            indices = sid_stp_indices.2.clone();
            gene_expression_headers = false;
        };
        println!("indices: {:?}", indices);
        if within_dataset_table && !gene_expression_headers {
            if thisline.starts_with("!dataset_table_end") {
                break 'linereading;
            }
            process_gene_expresssion_data(&thisline, &indices, &SIF);
        }
        if within_headers {
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
