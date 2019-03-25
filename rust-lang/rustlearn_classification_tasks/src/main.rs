extern crate serde;
// This lets us write `#[derive(Deserialize)]`.
#[macro_use]
extern crate serde_derive;

use std::io;
use std::process;
use std::vec::Vec;
use std::error::Error;

use csv;
use rand;
use rand::thread_rng;
use rand::seq::SliceRandom;

use rustlearn::prelude::*;
use rustlearn::ensemble::random_forest::Hyperparameters as randomforest;
use rustlearn::trees::decision_tree;
use rustlearn::linear_models::sgdclassifier::Hyperparameters as logistic_regression;
use rustlearn::svm::libsvm::svc::{Hyperparameters as libsvm_svc, KernelType};
use rustlearn::metrics::accuracy_score;

use xgboost;
use xgboost::{parameters, DMatrix, Booster};

fn main() {
    if let Err(err) = read_csv() {
        println!("{}", err);
        process::exit(1);
    }
}

#[derive(Debug, Deserialize)]
struct Flower {
    sepal_length: f32, // everything needs to be f32, other types wont do in rusty machine
    sepal_width: f32,
    petal_length: f32,
    petal_width: f32,
    species: String,
}

impl Flower {
    fn into_feature_vector(&self) -> Vec<f32> {
        vec![self.sepal_length, self.sepal_width, self.sepal_length, self.petal_width]
    }

    fn into_labels(&self) -> f32 {
        match self.species.as_str() {
            "setosa" => 0.,
            "versicolor" => 1.,
            "virginica" => 2.,
            l => panic!("Not able to parse the label. Some other label got passed. {:?}", l),
        }
    }
}

fn read_csv() -> Result<(), Box<Error>> {
    // Get all the data
    let mut rdr = csv::Reader::from_reader(io::stdin());
    let mut data = Vec::new();
    for result in rdr.deserialize() {
        let r: Flower = result?;
        data.push(r); // data contains all the records
    }

    // shuffle the data.
    data.shuffle(&mut thread_rng());

    // separate out to train and test datasets.
    let test_size: f32 = 0.2;
    let test_size: f32 = data.len() as f32 * test_size;
    let test_size = test_size.round() as usize;
    let (test_data, train_data) = data.split_at(test_size);
    let train_size = train_data.len();
    let test_size = test_data.len();

    // differentiate the features and the labels.
    let flower_x_train: Vec<f32> = train_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_train: Vec<f32> = train_data.iter().map(|r| r.into_labels()).collect();

    let flower_x_test: Vec<f32> = test_data.iter().flat_map(|r| r.into_feature_vector()).collect();
    let flower_y_test: Vec<f32> = test_data.iter().map(|r| r.into_labels()).collect();

    // Since rustlearn works with arrays we need to convert the vectors to a dense matrix or a sparse matrix
    let mut flower_x_train = Array::from(flower_x_train); // as opposed to rusty machine, all floats here are f32 reference : https://github.com/maciejkula/rustlearn/blob/7daf692fe504966aa84d920321b884afe19caa79/src/array/dense.rs#L129
    flower_x_train.reshape(train_size, 4);

    let flower_y_train = Array::from(flower_y_train);

    let mut flower_x_test = Array::from(flower_x_test);
    flower_x_test.reshape(test_size, 4);

    let flower_y_test = Array::from(flower_y_test);

    // create a random forest model
    let mut tree_params = decision_tree::Hyperparameters::new(flower_x_train.cols());
    tree_params.min_samples_split(10)
        .max_features(4);

    let mut model = randomforest::new(tree_params, 10).one_vs_rest();

    model.fit(&flower_x_train, &flower_y_train).unwrap();

    // Optionally serialize and deserialize the model

    // let encoded = bincode::rustc_serialize::encode(&model,
    //                                               bincode::SizeLimit::Infinite).unwrap();
    // let decoded: OneVsRestWrapper<RandomForest> = bincode::rustc_serialize::decode(&encoded).unwrap();

    let prediction = model.predict(&flower_x_test).unwrap();

    let accuracy = accuracy_score(&flower_y_test, &prediction);

    println!("Random Forest: accuracy: {:?}", accuracy);

    // working with Stochastic Gradient descent.
    // uses adaptive per parameter learning rate Adagrad
    let mut model = logistic_regression::new(4)
        .learning_rate(1.0)
        .l2_penalty(0.5)
        .l1_penalty(0.0)
        .one_vs_rest();
    let num_epochs = 100;

    for _ in 0..num_epochs {
        model.fit(&flower_x_train, &flower_y_train).unwrap();
    }

    let prediction = model.predict(&flower_x_test).unwrap();
    let accuracy = accuracy_score(&flower_y_test, &prediction);
    println!("Logistic Regression: accuracy: {:?}", accuracy);

    // Working with svms
    let svm_linear_model = libsvm_svc::new(4, KernelType::Linear, 3)
        .C(0.3)
        .build();
    let svm_poly_model = libsvm_svc::new(4, KernelType::Polynomial, 3)
        .C(0.3)
        .build();
    let svm_rbf_model = libsvm_svc::new(4, KernelType::RBF, 3)
        .C(0.3)
        .build();
    let svm_sigmoid_model = libsvm_svc::new(4, KernelType::Sigmoid, 3)
        .C(0.3)
        .build();
    let svm_kernel_types = ["linear", "polynomial", "rbf", "sigmoid"];
    let mut svm_model_types = [svm_linear_model, svm_poly_model, svm_rbf_model, svm_sigmoid_model];
    for (kernel_type, svm_model) in svm_kernel_types.iter().zip(svm_model_types.iter_mut()) {
        svm_model.fit(&flower_x_train, &flower_y_train).unwrap();

        let prediction = svm_model.predict(&flower_x_test).unwrap();
        let accuracy = accuracy_score(&flower_y_test, &prediction);
        println!("Lib svm {kernel}: accuracy: {accuracy}", accuracy=accuracy, kernel=kernel_type);
    };

    let x_train = &[1.0, 1.0, 1.0,
                    1.0, 1.0, 0.0,
                    1.0, 1.0, 1.0,
                    0.0, 0.0, 0.0,
                    1.0, 1.0, 1.0];
    let num_rows = 5;
    let y_train = &[1.0, 1.0, 1.0, 0.0, 1.0];

    // convert training data into XGBoost's matrix format
    let mut dtrain = DMatrix::from_dense(x_train, num_rows).unwrap();

    // set ground truth labels for the training matrix
    dtrain.set_labels(y_train).unwrap();

    // // test matrix with 1 row
    // let x_test = &[0.7, 0.9, 0.6];
    // let num_rows = 1;
    // let y_test = &[1.0];
    // let mut dtest = DMatrix::from_dense(x_test, num_rows).unwrap();
    // dtest.set_labels(y_test).unwrap();

    // configure objectives, metrics, etc.
    let learning_params = parameters::learning::LearningTaskParametersBuilder::default()
        .objective(parameters::learning::Objective::BinaryLogistic)
        .build().unwrap();

    // configure the tree-based learning model's parameters
    let tree_params = parameters::tree::TreeBoosterParametersBuilder::default()
            .max_depth(2)
            .eta(1.0)
            .build().unwrap();

    // overall configuration for Booster
    let booster_params = parameters::BoosterParametersBuilder::default()
        .booster_type(parameters::BoosterType::Tree(tree_params))
        .learning_params(learning_params)
        .verbose(true)
        .build().unwrap();

    // specify datasets to evaluate against during training
    let evaluation_sets = &[(&dtrain, "train"), (&dtest, "test")];

    // overall configuration for training/evaluation
    let params = parameters::TrainingParametersBuilder::default()
        .dtrain(&dtrain)                         // dataset to train with
        .boost_rounds(2)                         // number of training iterations
        .booster_params(booster_params)          // model parameters
        .evaluation_sets(Some(evaluation_sets)) // optional datasets to evaluate against in each iteration
        .build().unwrap();

    // train model, and print evaluation data
    let bst = Booster::train(&params).unwrap();

    println!("{:?}", bst.predict(&dtest).unwrap());

    Ok(())
}