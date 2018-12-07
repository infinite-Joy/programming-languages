#[macro_use(array)]
extern crate ndarray;

use ndarray::prelude::*;
use ndarray::{arr1, arr2, Array1, ArrayView1, Array2};

// references: https://docs.rs/ndarray/*/ndarray/doc/ndarray_for_numpy_users/index.html#mathematics
// https://github.com/rust-ndarray/ndarray/blob/master/examples/column_standardize.rs
// https://gist.github.com/samueljackson92/8148506

//fn compute_cost(X: &Array2<f64>, y: ArrayView1<f64>, theta: &mut Array1<f64>) -> Array1<f64> {
fn compute_cost(X: &Array2<f64>, y: ArrayView1<f64>, theta: &Array1<f64>) -> Array1<f64> {
//fn compute_cost(X: &Array2<f64>, y: ArrayView1<f64>, theta: ArrayView1<f64>) -> f64 {
    // we need array2 for 2 dim array.
    // python function
    //diffs = np.power(((X @ theta.T)-y),2);
    //np.sum(diffs)/(2 * len(X))
    //----------------

    let alpha = 0.001;
    let n = X.len() as f64;
    let theta_transposed = theta.t();
    //println!("dimension of theta {:#?}", theta.shape());
    //println!("dimension of theta {:#?}", theta_transposed.shape());

    let predicted = X.dot(&theta_transposed);
    //println!("predicted done {:#?}", predicted);
    //println!("target {:#?}", y);
    let diffs = predicted - y;
    //println!("diffs: {:#?}", diffs);
    let cost_squared = diffs.mapv(|a| a.powi(2));
    let present_cost = (cost_squared.sum()) / (2. * n);
    //println!("Cost is {}", present_cost);

    //calculate averge gradient for every example
    //gradient = np.dot(xs_transposed, diffs) / num_examples
    let xs_transposed = X.t();
    let gradient = xs_transposed.dot(&diffs).sum();
    //println!("present gradient {}", gradient);
    let updated_theta = theta.mapv(|a| a - alpha*gradient/n);
    //println!("{:#?}", updated_theta);
    updated_theta
}

fn predict(X: &Array2<f64>, theta: ArrayView1<f64>) -> Array1<f64> {
    let theta_transposed = theta.t();
    X.dot(&theta_transposed)
    
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
    //println!("{}", new_vec);

    let new_matrix = matrix.dot(&new_vec);
    //println!("{}", new_matrix);

    //let mut data = array![[-1., -2., -3.],
    //                      [ 1., -3.,  5.],
    //                      [ 2.,  2.,  2.],
    //                      [ 3.,  4.,  5.]];
    //let y = array![-6., -3., 6., 12.];
    let mut data = array![[5.1,3.5,1.4,0.2],
                          [4.9,3.0,1.4,0.2],
                          [4.7,3.2,1.3,0.2],
                          [4.6,3.1,1.5,0.2],
                          [5.0,3.6,1.4,0.2],
                          [5.4,3.9,1.7,0.4],
                          [4.6,3.4,1.4,0.3],
                          [5.0,3.4,1.5,0.2],
                          [4.4,2.9,1.4,0.2],
                          [4.9,3.1,1.5,0.1],
                          [5.4,3.7,1.5,0.2],
                          [4.8,3.4,1.6,0.2],
                          [4.8,3.0,1.4,0.1],
                          [4.3,3.0,1.1,0.1],
                          [5.8,4.0,1.2,0.2],
                          [5.7,4.4,1.5,0.4],
                          [5.4,3.9,1.3,0.4],
                          [5.1,3.5,1.4,0.3],
                          [5.7,3.8,1.7,0.3],
                          [5.1,3.8,1.5,0.3],
                          [5.4,3.4,1.7,0.2],
                          [5.1,3.7,1.5,0.4],
                          [4.6,3.6,1.0,0.2],
                          [5.1,3.3,1.7,0.5],
                          [4.8,3.4,1.9,0.2],
                          [5.0,3.0,1.6,0.2],
                          [5.0,3.4,1.6,0.4],
                          [5.2,3.5,1.5,0.2],
                          [5.2,3.4,1.4,0.2],
                          [4.7,3.2,1.6,0.2],
                          [4.8,3.1,1.6,0.2],
                          [5.4,3.4,1.5,0.4],
                          [5.2,4.1,1.5,0.1],
                          [5.5,4.2,1.4,0.2],
                          [4.9,3.1,1.5,0.1],
                          [5.0,3.2,1.2,0.2],
                          [5.5,3.5,1.3,0.2],
                          [4.9,3.1,1.5,0.1],
                          [4.4,3.0,1.3,0.2],
                          [5.1,3.4,1.5,0.2],
                          [5.0,3.5,1.3,0.3],
                          [4.5,2.3,1.3,0.3],
                          [4.4,3.2,1.3,0.2],
                          [5.0,3.5,1.6,0.6],
                          [5.1,3.8,1.9,0.4],
                          [4.8,3.0,1.4,0.3],
                          [5.1,3.8,1.6,0.2],
                          [4.6,3.2,1.4,0.2],
                          [5.3,3.7,1.5,0.2],
                          [5.0,3.3,1.4,0.2],
                          [7.0,3.2,4.7,1.4],
                          [6.4,3.2,4.5,1.5],
                          [6.9,3.1,4.9,1.5],
                          [5.5,2.3,4.0,1.3],
                          [6.5,2.8,4.6,1.5],
                          [5.7,2.8,4.5,1.3],
                          [6.3,3.3,4.7,1.6],
                          [4.9,2.4,3.3,1.0],
                          [6.6,2.9,4.6,1.3],
                          [5.2,2.7,3.9,1.4],
                          [5.0,2.0,3.5,1.0],
                          [5.9,3.0,4.2,1.5],
                          [6.0,2.2,4.0,1.0],
                          [6.1,2.9,4.7,1.4],
                          [5.6,2.9,3.6,1.3],
                          [6.7,3.1,4.4,1.4],
                          [5.6,3.0,4.5,1.5],
                          [5.8,2.7,4.1,1.0],
                          [6.2,2.2,4.5,1.5],
                          [5.6,2.5,3.9,1.1],
                          [5.9,3.2,4.8,1.8],
                          [6.1,2.8,4.0,1.3],
                          [6.3,2.5,4.9,1.5],
                          [6.1,2.8,4.7,1.2],
                          [6.4,2.9,4.3,1.3],
                          [6.6,3.0,4.4,1.4],
                          [6.8,2.8,4.8,1.4],
                          [6.7,3.0,5.0,1.7],
                          [6.0,2.9,4.5,1.5],
                          [5.7,2.6,3.5,1.0],
                          [5.5,2.4,3.8,1.1],
                          [5.5,2.4,3.7,1.0],
                          [5.8,2.7,3.9,1.2],
                          [6.0,2.7,5.1,1.6],
                          [5.4,3.0,4.5,1.5],
                          [6.0,3.4,4.5,1.6],
                          [6.7,3.1,4.7,1.5],
                          [6.3,2.3,4.4,1.3],
                          [5.6,3.0,4.1,1.3],
                          [5.5,2.5,4.0,1.3],
                          [5.5,2.6,4.4,1.2],
                          [6.1,3.0,4.6,1.4],
                          [5.8,2.6,4.0,1.2],
                          [5.0,2.3,3.3,1.0],
                          [5.6,2.7,4.2,1.3],
                          [5.7,3.0,4.2,1.2],
                          [5.7,2.9,4.2,1.3],
                          [6.2,2.9,4.3,1.3],
                          [5.1,2.5,3.0,1.1],
                          [5.7,2.8,4.1,1.3],
                          [6.3,3.3,6.0,2.5],
                          [5.8,2.7,5.1,1.9],
                          [7.1,3.0,5.9,2.1],
                          [6.3,2.9,5.6,1.8],
                          [6.5,3.0,5.8,2.2],
                          [7.6,3.0,6.6,2.1],
                          [4.9,2.5,4.5,1.7],
                          [7.3,2.9,6.3,1.8],
                          [6.7,2.5,5.8,1.8],
                          [7.2,3.6,6.1,2.5],
                          [6.5,3.2,5.1,2.0],
                          [6.4,2.7,5.3,1.9],
                          [6.8,3.0,5.5,2.1],
                          [5.7,2.5,5.0,2.0],
                          [5.8,2.8,5.1,2.4],
                          [6.4,3.2,5.3,2.3],
                          [6.5,3.0,5.5,1.8],
                          [7.7,3.8,6.7,2.2],
                          [7.7,2.6,6.9,2.3],
                          [6.0,2.2,5.0,1.5],
                          [6.9,3.2,5.7,2.3],
                          [5.6,2.8,4.9,2.0],
                          [7.7,2.8,6.7,2.0],
                          [6.3,2.7,4.9,1.8],
                          [6.7,3.3,5.7,2.1],
                          [7.2,3.2,6.0,1.8],
                          [6.2,2.8,4.8,1.8],
                          [6.1,3.0,4.9,1.8],
                          [6.4,2.8,5.6,2.1],
                          [7.2,3.0,5.8,1.6],
                          [7.4,2.8,6.1,1.9],
                          [7.9,3.8,6.4,2.0],
                          [6.4,2.8,5.6,2.2],
                          [6.3,2.8,5.1,1.5],
                          [6.1,2.6,5.6,1.4],
                          [7.7,3.0,6.1,2.3],
                          [6.3,3.4,5.6,2.4],
                          [6.4,3.1,5.5,1.8],
                          [6.0,3.0,4.8,1.8],
                          [6.9,3.1,5.4,2.1],
                          [6.7,3.1,5.6,2.4],
                          [6.9,3.1,5.1,2.3],
                          [5.8,2.7,5.1,1.9],
                          [6.8,3.2,5.9,2.3],
                          [6.7,3.3,5.7,2.5],
                          [6.7,3.0,5.2,2.3],
                          [6.3,2.5,5.0,1.9],
                          [6.5,3.0,5.2,2.0],
                          [6.2,3.4,5.4,2.3],
                          [5.9,3.0,5.1,1.8]];
    let y = array![0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.];
    //println!("The original data.");
    //println!("{:8.4}", data);
    //println!("{:8.4} (Mean axis=0)", data.mean_axis(Axis(0)));

    data -= &data.mean_axis(Axis(0));
    //println!("{:8.4}", data);

    data /= &std(&data, Axis(0));
    //println!("After mean normalisation.");
    //println!("{:8.4}", data);

    //println!("||y||_2 = {:#?}", l2_norm(y.view()));
    //println!("||y||_1 = {:#?}", l1_norm(y.view()));
    //println!("normalizing y yields {:#?}", normalize(&y));

    let n = data.dim();
    let iters = 1000;
    let ones_vec = vec![1. as f64; n.1];
    //assert_eq!(ones_vec.len(), 3);
    //println!("this is the len of ones_vec {}", ones_vec.len());
    let mut thetas = Array::from_vec(ones_vec);
    for _ in 0..iters {
        thetas = compute_cost(&data, y.view(), &thetas);
        //println!("present thetas {}", thetas);
    }
    ////println!("output compute_cost {}", compute_cost(&data, y.view(), thetas.view()));
    let testdata = array![[5.1,3.5,1.4,0.2],
                          [5.9,3.0,5.1,1.8]];
    println!("predicted output {}", predict(&testdata, thetas.view()))
}
