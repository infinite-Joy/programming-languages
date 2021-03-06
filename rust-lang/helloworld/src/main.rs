use std::ops:: Add;

fn index<T: PartialEq>(slice: &[T], target: &T) -> Option<usize> {
    for (index, element) in slice.iter().enumerate() {
        if element == target {
            return Some(index)
        }
    }
    None
}

fn min_max(slice: &[i32]) -> Option<(i32, i32)> {
    if slice.is_empty() {
        return None;
    }
    let mut min = slice[0];
    let mut max = slice[0];
    for &element in slice {
        if element < min {
            min = element;
        }
        if element > max {
            max = element;
        }
    }
    Some((min, max))
    
}

fn first<T>(slice: &[T]) -> &T {
    &slice[0]

}

fn max<T: PartialOrd>(a: T, b: T) -> T {
    if a > b {
        a
    } else {
        b
    }
}

//enum Option<T> {
//    Some(T),
//    None,
//}

trait BitSet {
    fn clear(&mut self, index: usize);
    fn is_set(&self, index: usize) -> bool;
    fn set(&mut self, index: usize);

    fn toggle(&mut self, index: usize) {
        if self.is_set(index) {
            println!("will clear {}", index);
            self.clear(index);
        } else {
            println!("will set {}", index);
            self.set(index);
        }
        
    }
    
}

impl BitSet for u64 {
    fn clear(&mut self, index: usize) {
        *self &= !(1 << index);
    }
    fn is_set(&self, index: usize) -> bool {
        (*self >> index) & 1 == 1
    }
    fn set(&mut self, index: usize) {
        *self |= 1 << index;
    }
}

fn upppercase(c: u8) -> u8 {
    match c {
        b'a'...b'z' => c - 32,
        _ => c,
    }
    
}

fn is_alphanumeric(c: char) -> bool {
    match c {
        'a'...'z' | 'A'...'Z' | '0'...'9' => true,
        _ => false,
    }
    
}
enum Expr {
    Null,
    Add(i32, i32),
    Sub(i32, i32),
    Mul(i32, i32),
    Div{ dividend: i32, divisor: i32},
    Val(i32),

}

fn print_expr(expr: Expr) {
    match expr {
        Expr::Null => println!("No Value"),
        Expr::Add(x, y) => println!("{}", x + y),
        Expr::Sub(x, y) => println!("{}", x - y),
        Expr::Mul(x, y) => println!("{}", x * y),
        Expr::Div{dividend: x, divisor: 0} => println!("Divisor is 0"),
        Expr::Div{dividend: x, divisor: y} => println!("{}", x/y),
        Expr::Val(x) => println!("{}", x),
    }
    
}

fn inc_x(point: &mut Point) {
    point.x += 1;
}

//fn max(a: i32, b: i32) -> i32 {
//    if a > b {
//        a
//    } else {
//        b
//    }
//}

fn print_point(point: &Point) {
    println!("This is inside the function");
    println!("x: {}, y: {}", point.x, point.y);
    println!("##########################");
}

struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Self {
        Self {x, y}
        
    }
    fn distance_from_origin(&self) -> f64 {
        let sum_of_squares = self.x.pow(2) + self.y.pow(2);
        (sum_of_squares as f64).sqrt()
    }

    fn translate(&mut self, dx: i32, dy: i32) {
        self.x += dx;
        self.y += dy;
    }
}

impl Add<Point> for Point {
    type Output = Point;

    fn add(self, point: Point) -> Self::Output {
        Point {
            x: self.x + point.x,
            y: self.y + point.y,
        }
    }
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
    println!("{}", n2);

    let mut p1 = Point { x: 1, y: 2 };
    println!("value of p1 before inc {}", p1.x);
    inc_x(&mut p1);
    println!("value of p1 after inc {}", p1.x);

    let point = Point { x: 24, y: 42 };
    println!("({}, {})", point.x, point.y);
    println!("Distance from origin {}", point.distance_from_origin());

    // tuples
    let tuple = (24, 42);
    println!("({} {})", tuple.0, tuple.1);
    let (hello, world) = "helloworld".split_at(5);
    println!("{} {}!", hello, world);

    let quotient = Expr::Div{ dividend: 10, divisor: 2 };
    let sum = Expr::Add(40, 2);

    println!("Printing out the expressions.");
    print_expr(quotient);
    print_expr(sum);

    println!("{}", upppercase(b'j') as char);
    println!("{}", is_alphanumeric('j'));

    println!("Trying out traits.");
    let mut num = 0;
    num.set(15);
    println!("{}", num.is_set(15));
    num.clear(15);
    num.toggle(16);
    num.toggle(16);
    println!("done with the traits.");

    println!("Associated types");
    let p1 = Point {x: 1, y: 2};
    let p2 = Point {x: 3, y: 4};
    let p3 = p1 + p2;
    println!("({}, {})", p3.x, p3.y);
    println!("{}", max('a', 'z'));

    let array: [i16; 4] = [1, 2, 3, 4];
    println!("{}", array[3]);

    println!("Slices are fat pointers");
    println!("first of the array {}", first(&array));
    println!("first of the array {}", first(&array[2..]));

    println!("for loops");
    let array = [1, 2, 3, 4];
    let mut sum = 0;
    for element in &array {
        sum += *element;
    }
    println!("Sum: {}", sum);

    println!("min max: {:#?}", min_max(&array));



}
