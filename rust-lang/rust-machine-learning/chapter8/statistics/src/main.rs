#![allow(non_snake_case)]

use std::path::Path;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;
use std::f64;

use ndarray;
use ndarray::{Array, ArrayBase, Array2, Array1, Axis, arr2, stack};
use ndarray::prelude::*;

// https://nbviewer.jupyter.org/urls/umich.box.com/shared/static/7kh8amlez7bx3qlqa6aa.ipynb?create=1

fn process_gene_expresssion_data_headers(thisline: &String, SIF: &HashMap<String, String>) -> (Vec<String>, Vec<String>, Vec<usize>) {
    println!(" this line: {:?}", thisline);
    let SID: Vec<String> = thisline.split("\t").map(|s| s.to_owned()).collect();
    let indices: Vec<usize> = SID.iter()
                .enumerate()
                .filter(|&(_, x)| x.starts_with("GSM") )
                .map(|(i, _)| i).collect();
    let SID: Vec<String> = indices.iter().map(|&i| SID[i].clone()).collect();
    // println!(" sid: {:?}", SID);
    let STP: Vec<String> = SID.iter().map(
        |k| SIF.get(&k.to_string()).unwrap())
        .cloned().collect();
    // println!(" STP: {:?}", STP);
    (SID, STP, indices)
}

/// Read the gene expression data as a list of lists, also get the gene identifiers
fn process_gene_expresssion_data(thisline: &String, indices: &Vec<usize>, SIF: &HashMap<String, String>) -> (Vec<f64>, String) {
    let gene_expression_measure_values: Vec<String> = thisline.split("\t")
        .map(|s| s.to_owned()).collect();
    // println!("gene_expression_measure_values {:?}", gene_expression_measure_values);
    let gene_expression_measures = indices.iter().map(|&i| gene_expression_measure_values[i].clone());
    let gene_expression_measures: Vec<f64> = gene_expression_measures.map(|x| x.parse().unwrap()).collect();
    let gene_identifiers = vec![gene_expression_measure_values[0].clone(), gene_expression_measure_values[1].clone()].join(";");
    (gene_expression_measures, gene_identifiers)
}

fn filter_specific_samples(STP: &Vec<String>, group_type: &str) -> Vec<usize> {
    STP.iter().enumerate()
        .filter(|&(_, x)| x == group_type )
        .map(|(i, _)| i).collect()
}

fn different_samples(STP: &Vec<String>) -> (Vec<usize>, Vec<usize>) {
    let UC = filter_specific_samples(&STP, "ulcerative colitis");
    let CD = filter_specific_samples(&STP, "Crohn's disease");
    (UC, CD)
}

fn convert_to_log_scale(X: &Array2<f64>) -> Array2<f64> {
    let two = 2.0f64;
    let two_log = two.ln();
    X.mapv(|x| x.ln()/two_log)
}


fn process_file(filename: &Path) -> io::Result<HashMap<String, String>> {
    let mut SIF = HashMap::new();
    let file = File::open(filename).unwrap();
    let mut subset_description = String::new();
    let mut within_dataset_table = false;
    let mut within_headers = true;
    let mut gene_expression_headers = true;
    let mut indices: Vec<usize> = Vec::new();
    let mut gene_expression_measures_vec = Vec::new();
    let mut gene_identifiers_vec = Vec::new();
    let mut SID = Vec::new();
    let mut STP = Vec::new();
    'linereading: for line in BufReader::new(file).lines() {
        let thisline = line?;
        let line_split: Vec<String> = thisline.split("=").map(|s| s.to_owned()).collect();
        // println!("this line: {:?}", thisline);
        if thisline.starts_with("!dataset_table_begin") {
            within_dataset_table = true;
            within_headers = false;
            continue 'linereading;
        }
        // let mut SID: Vec<String> = Vec::new();
        // let mut SID: Vec<String> = Vec::new();
        // let mut SID: Vec<usize> = Vec::new();
        if within_dataset_table && gene_expression_headers {
            // println!("wihting within_dataset_table && gene_expression_headers", );
            let sid_stp_indices = process_gene_expresssion_data_headers(&thisline, &SIF);
            indices = sid_stp_indices.2.clone();
            SID = sid_stp_indices.0.clone();
            STP = sid_stp_indices.1.clone();
            gene_expression_headers = false;
            continue 'linereading;
        };
        // println!("indices: {:?}", indices);
        if within_dataset_table && !gene_expression_headers {
            if thisline.starts_with("!dataset_table_end") {
                break 'linereading;
            }
            let (gene_expression_measures, gene_identifiers) = process_gene_expresssion_data(&thisline, &indices, &SIF);
            gene_expression_measures_vec.extend(gene_expression_measures);
            gene_identifiers_vec.push(gene_identifiers);
        }
        if within_headers {
            if thisline.starts_with("!subset_description") {
                subset_description = line_split[1].trim().to_owned();
            };
            // println!("subset description {:?}", subset_description);
            let subset_ids = if thisline.starts_with("!subset_sample_id") {
                let subset_ids = line_split[1].split(",");
                let subset_ids = subset_ids.map(|s| s.trim().to_owned());
                subset_ids.collect()
            } else {
                Vec::new()
            };
            // println!("subset ids {:?}", subset_ids);
            for k in subset_ids {
                SIF.insert(k, subset_description.to_owned());
                // println!("SIF: {:?}", SIF);
            }
        }
    }
    // println!("gene expression len {}", gene_expression_measures_vec.len());
    // panic!();
    let gene_expression_measures_matrix = Array::from_shape_vec((22283, 127), gene_expression_measures_vec).unwrap();
    let gene_expression_measures_matrix = convert_to_log_scale(&gene_expression_measures_matrix);
    let (UC, CD) = different_samples(&STP);
    println!("{:?}", gene_expression_measures_matrix.shape());
    println!("UC {:?}", UC);
    let mut cols = Vec::new();
    for muc_columns in UC {
        let col = gene_expression_measures_matrix.column(muc_columns);
        cols.push(col);
        // let col_mean = col.mean_axis(Axis(1));
        // println!("col_mean {:?}", col_mean);
    }
    println!("{:?}", cols.len());
    let MUC = stack(Axis(0), &cols[..]).unwrap();
    let MUC = Array::from_iter(MUC.iter());
    println!("{:?}", MUC.shape());
    let MUC = MUC.into_shape((22283, 26)).unwrap();
    let MUC = MUC.t();

    // let MUC: Vec<Array1<f64>> = UC.iter().map(|&c| gene_expression_measures_matrix.column(c)).collect();
    // println!("MUC {:?}", MUC);
    // let MUC_4 = gene_expression_measures_matrix.column(42);
    // println!("MUC {:?}", );

    let a = arr2(&[[1.,2.,3.], [4.,5.,6.]]);
    let b = stack(Axis(0), &[a.column(1).view(), a.column(2).view()]).unwrap();
    let b = Array::from_iter(b.iter());
    println!("{:?}", b);
    let b = b.into_shape((2, 2)).unwrap();
    let b = b.t();
    println!("{:?}", b);
    println!("{:?}", b.column(0).fold(0.0f32, |a, &b| a + b));
    Ok(SIF)
}

fn main() {
    let filename = Path::new("GDS1615_full.soft");
    process_file(&filename).unwrap();
}