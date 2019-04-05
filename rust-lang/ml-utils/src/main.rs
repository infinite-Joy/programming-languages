use std::vec::Vec;
use std::collections::HashMap;
// use std::io::Error;
use std::error::Error;
use std::cmp::Ordering;

use rand;
use rand::distributions::{Bernoulli, Distribution};
use itertools;
use itertools::iproduct;
use itertools::Itertools;

fn contingency_table(cluster1: &Vec<Vec<f64>>, cluster2: &Vec<Vec<f64>>) -> Vec<std::vec::Vec<usize>> {
    let length = cluster1.len();
    assert!(length == cluster2.len());
    let product = iproduct!(cluster1, cluster2);
    let cont_table_vec: Vec<usize> = product.map(
        |(c1, c2)| match c1.len().cmp(&c2.len()) {
            Ordering::Less => c1.len(),
            _ => c2.len(),
        }
    ).collect();
    let v_chunked: Vec<Vec<usize>> = cont_table_vec.chunks(length).map(|x| x.to_vec()).collect();
    return v_chunked;
}

fn main() {
    let cluster1 = vec![vec![0.0f64,3.0,5.0, 6.0, 8.0], vec![1.0f64,7.0], vec![2.0f64,4.0]];
    let cluster2 = vec![vec![0.0f64,1.0], vec![2.0f64,5.0,6.0, 8.0], vec![3.0f64,4.0,7.0]];
    let table = contingency_table(&cluster1, &cluster2);
    println!("{:?}", table);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_contingency_table() {
        let cluster1 = vec![vec![0.0f64,3.0,5.0, 6.0, 8.0], vec![1.0f64,7.0], vec![2.0f64,4.0]];
        let cluster2 = vec![vec![0.0f64,1.0], vec![2.0f64,5.0,6.0, 8.0], vec![3.0f64,4.0,7.0]];
        let table = contingency_table(&cluster1, &cluster2);
        assert_eq!(table, [[2, 4, 3], [2, 2, 2], [2, 2, 2]]);
    }
}