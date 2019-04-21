use ndarray;
use ndarray::prelude::*;

fn main() {
    let a1 = arr2(&[[0., 1., 2.],
                    [3., 4., 5.]]);
    println!("{:?}", a1);

    let a2 = Array::from_shape_vec((2, 3).strides((3, 1)),
        vec![0., 1., 2., 3., 4., 5.]).unwrap();
    assert!(a1 == a2);
}
