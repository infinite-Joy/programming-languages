use std::io;

fn celsius_to_fahrenheit(num: f32) -> f32 {
    num * 1.8 + 32.0
    
}

fn fahrenheit_to_celsius(num: f32) -> f32 {
    (num - 32.0) * 0.5556

}

fn read_user_input() -> f32 {
    let mut user_input = String::new();
    io::stdin().read_line(&mut user_input)
        .expect("Failed to read line");
    let user_input: f32 = user_input.trim().parse()
        .expect("Please type a number!");
    user_input
    
}

fn main() {
    println!("Specify the type of converter.");
    println!("==============================");
    println!("1. Celsius to Fahrenheit");
    println!("2. Fahrenheit to Celsius.");

    let conversion_type = read_user_input();
    println!("Now provide the target number that you wish to convert.");
    let target_number = read_user_input();

    if conversion_type == 1.0 {
        let result = celsius_to_fahrenheit(target_number);
        println!("Celsius: {} => Fahrenheit {}", target_number, result );
    } else if conversion_type == 2.0 {
        let result = fahrenheit_to_celsius(target_number);
        println!("Fahrenheit: {} => Celsius {}", target_number, result );
    } else {
        println!("You have not chosen a valid input. Please check the menu above!!");
    }
}
