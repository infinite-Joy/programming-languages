use crfsuite::{Model, Attribute, CrfError};
use crfsuite::{Trainer, Algorithm, GraphicalModel};

// data from here https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus

fn main() {
    let xseq = vec![
        vec![Attribute::new("walk", 1.0), Attribute::new("shop", 0.5)],
        vec![Attribute::new("walk", 1.0)],
        vec![Attribute::new("walk", 1.0), Attribute::new("clean", 0.5)],
        vec![Attribute::new("shop", 0.5), Attribute::new("clean", 0.5)],
        vec![Attribute::new("walk", 0.5), Attribute::new("clean", 1.0)],
        vec![Attribute::new("clean", 1.0), Attribute::new("shop", 0.1)],
        vec![Attribute::new("walk", 1.0), Attribute::new("shop", 0.5)],
        vec![],
        vec![Attribute::new("clean", 1.0)],
    ];
    let yseq = ["sunny", "sunny", "sunny", "rainy", "rainy", "rainy", "sunny", "sunny", "rainy"];
    let mut trainer = Trainer::new(true);
    trainer.select(Algorithm::LBFGS, GraphicalModel::CRF1D).unwrap();
    trainer.append(&xseq, &yseq, 0i32).unwrap();
    trainer.train("test.crfsuite", -1i32).unwrap();
    drop(trainer);

    // tag
    let model = Model::from_file("test.crfsuite").unwrap();
    let mut tagger = model.tagger().unwrap();
    let res = tagger.tag(&xseq).unwrap();
    assert_eq!(res, yseq);




    // let model_memory = include_bytes!("/home/nineleaps/thinking/programming-languages/rust-lang/chapter5/crfsuite-0.12/crfsuite-0.12/example/CoNLL2000.model");
    // let model = Model::from_memory(&model_memory[..]).unwrap();
    // let mut tagger = model.tagger().unwrap();
    // let xseq = vec![
    //     vec![Attribute::new("I", 1.0), Attribute::new("am", 0.5)],
    //     vec![Attribute::new("pound", 1.0)],
    //     vec![Attribute::new("pound", 1.0), Attribute::new("in", 0.5)],
    //     vec![Attribute::new("shop", 0.5), Attribute::new("to", 0.5)],
    //     vec![Attribute::new("buy", 0.5), Attribute::new("new", 1.0)],
    //     vec![Attribute::new("clothes", 1.0), Attribute::new("thank", 0.1)],
    //     vec![Attribute::new("you", 1.0), Attribute::new("for", 0.5)],
    //     vec![],
    //     vec![Attribute::new("help", 1.0)],
    // ];
    // // let yseq = ["Going", "to", "the", "market"];
    // let yseq = ["B-NP", "I-NP", "I-NP", "I-NP", "I-NP", "I-NP", "I-NP", "I-NP", "I-NP"];
    // let res = tagger.tag(&xseq).unwrap();
    // // assert_eq!(res, yseq);

    // let x = tagger.probability(&yseq).unwrap();
    // println!("{:?}", x);
    // let y = tagger.marginal("I-NP", 1i32).unwrap();
    // println!("{:?}", y)
    // // assert!(false);
}
