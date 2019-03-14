// structures.rs
// $ ./structures
// Planet { co2: 0.04, nitrogen: 78.09 }
// Planet { co2: 95.32, nitrogen: 2.7 }

#[derive(Debug)]
struct Planet {
    co2: f32,
    nitrogen: f32
}

fn main() {
    let earth = Planet { co2: 0.04, nitrogen: 78.09 };
    println!("{:?}", earth);

    let mars = Planet { co2: 95.32, nitrogen: 2.7 };
    println!("{:?}", mars);
}