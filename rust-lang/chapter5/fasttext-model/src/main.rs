use fasttext::FastText;
use fasttext::Args;
use fasttext::Prediction;
use fasttext::{ModelName, LossName};

fn main() {
    let mut args = Args::new();
    // args.set_input("data/train.csv");
    args.set_input("cooking.train");
    args.set_output("output.model");
    args.set_model(ModelName::SUP);
    args.set_loss(LossName::SOFTMAX);
    println!("{:?}", args);
    let mut ft_model = FastText::new();
    ft_model.train(&args).unwrap();
    let preds = ft_model.predict("I am going to the end of the world", 2, 0.000000001).unwrap();
    println!("{:?}", preds);
    println!("Hello, world!");
}