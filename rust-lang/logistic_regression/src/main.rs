extern crate rustlearn;

use rustlearn::prelude::*;
use rustlearn::linear_models::sgdclassifier::Hyperparameters;
use rustlearn::cross_validation::CrossValidation;
use rustlearn::datasets::iris;
use rustlearn::metrics::accuracy_score;

fn main() {
    let (X, y) = iris::load_data();
    let num_splits = 10;
    let num_epochs = 5;
    let mut accuracy = 0.0;

    for (train_idx, test_idx) in CrossValidation::new(X.rows(), num_splits) {
        let X_train = X.get_rows(&train_idx);
        let y_train = y.get_rows(&train_idx);
        let X_test = X.get_rows(&test_idx);
        let y_test = y.get_rows(&test_idx);

        let mut model = Hyperparameters::new(X.cols())
                                    .learning_rate(0.5)
                                    .l2_penalty(0.0)
                                    .l1_penalty(0.0)
                                    .one_vs_rest();
        for _ in 0..num_epochs {
            model.fit(&X_train, &y_train).unwrap();
        }
        let prediction = model.predict(&X_test).unwrap();
        let present_acc = accuracy_score(&y_test, &prediction);
        accuracy += present_acc;
    }
    println!("accuracy: {:#?}", accuracy / num_splits as f32);
}
