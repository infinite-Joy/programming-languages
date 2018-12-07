#[macro_use(array)]
extern crate ndarray;

use ndarray::prelude::*;
use ndarray::{arr1, arr2, Array1, ArrayView1, Array2};

fn compute_cost(X: &Array2<f64>, y: ArrayView1<f64>, theta: ArrayView1<f64>) -> f64 {
    // we need array2 for 2 dim array.
    // python function
    //tobesummed = np.power(((X @ theta.T)-y),2);
    //np.sum(tobesummed)/(2 * len(X))
    //----------------

    let n = X.len() as f64;
    let theta_transposed = theta.t();
    let tobesummed = X.dot(&theta_transposed) - y;
    let cost_squared = tobesummed.mapv(|a| a.powi(2));
    (cost_squared.sum()) / (2. * n)
}

fn l1_norm(x: ArrayView1<f64>) -> f64 {
    x.fold(0., |acc, elem| acc + elem.abs())
}

fn l2_norm(x: ArrayView1<f64>) -> f64 {
    x.dot(&x).sqrt()
}

fn normalize(x: &Array1<f64>) -> Array1<f64> {
    let norm = l2_norm(x.view());
    let x_prime = x.mapv(|e| e/norm);
    x_prime
}

fn std1d(a: ArrayView1<f64>) -> f64 {
    let n = a.len() as f64;
    if n == 0. { return 0.; }
    let mean = a.sum() / n;
    (a.fold(0., |acc, &x| acc + (x - mean).powi(2)) / n).sqrt()
}

fn std(a: &Array2<f64>, axis: Axis) -> Array1<f64> {
    a.map_axis(axis, std1d)
}

fn main() {
    let scalar = 4;

    let vector = arr1(&[1, 2, 3]);

    let matrix = arr2(&[[4, 5, 6],
                      [7, 8, 9]]);

    let new_vec: Array1<_> = scalar * vector;
    println!("{}", new_vec);

    let new_matrix = matrix.dot(&new_vec);
    println!("{}", new_matrix);

    let mut data = array![[-1., -2., -3.],
                          [ 1., -3.,  5.],
                          [ 2.,  2.,  2.]];

    println!("The original data.");
    println!("{:8.4}", data);
    println!("{:8.4} (Mean axis=0)", data.mean_axis(Axis(0)));

    data -= &data.mean_axis(Axis(0));
    println!("{:8.4}", data);

    data /= &std(&data, Axis(0));
    println!("After mean normalisation.");
    println!("{:8.4}", data);

    let y = array![1., 2., 3.];
    println!("||y||_2 = {:#?}", l2_norm(y.view()));
    println!("||y||_1 = {:#?}", l1_norm(y.view()));
    println!("normalizing y yields {:#?}", normalize(&y));

    println!("output compute_cost {}", compute_cost(&data, y.view(), y.view()))

}
