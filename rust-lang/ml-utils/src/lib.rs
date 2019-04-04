fn generate_data(N_A: u32, N_B: u32, p_A: f64, p_B: f64) {
    // initiate empty container.
    // let data = vec![];

    //  total amount of rows in the data
    let N = N_A + N_B;
    println!("{:?}", N);
}

fn main() {
    generate_data(10, 10, 0.1, 0.02);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(generate_data(10, 10, 0.1, 0.02), ());
    }
}
