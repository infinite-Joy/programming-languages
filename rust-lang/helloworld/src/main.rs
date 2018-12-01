fn max(a: i32, b: i32) -> i32 {
    if a > b {
        a
    } else {
        b
    }
}

fn print_point(point: &Point) {
    println!("This is inside the function");
    println!("x: {}, y: {}", point.x, point.y);
    println!("##########################");
}

struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let name: &str = "world";
    println!("Hello, {}!", name);

    let num1 = 24;
    let num2 = 42;
    if num1 > num2 { // this expression must be a bool type
        println!("{} > {}",  num1, num2);
    } else {
        println!("{} <= {}",  num1, num2);
    }

    let mut a = 15;
    let mut b = 40;
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    println!("Greatest common divisor of 15 and 40 is: {}", a);

    let point = Point { x: 24, y: 42 };
    println!("({}, {})", point.x, point.y);

    println!("avoiding moving a variable by passing the reference");
    let p1 = Point { x: 1, y: 2 };
    let p2 = &p1;
    println!("{}", p1.x);
    println!("{}", p2.x);

    println!("references can also be passed as the type of a function parameter.");
    print_point(&p1);
    println!("x: {}, y: {}", p1.x, p1.y);

    println!("but an integer is a copy type.");
    let n1 = 42;
    let n2 = n1;
    println!("{}", n1);

}
