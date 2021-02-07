console.log('Hello world');

// simple function
function hello() { return "Hello" };
console.log(hello());


// convert this into async function
async function hello() { return "Hello" };
console.log(hello());
// interestingly now both the functions return promise

// you can also create an async function expression
let hello_arrow = async () => { return "hello from arrow" };
console.log(hello_arrow());

// to get the value we need to consume using function
hello_arrow().then((value) => console.log("value from hello arrow: ", value))

// so the async is added to functions to tell them to return a promise instead of directly
// returning the values

async function hello_2() {
    return greeting = await Promise.resolve("hello_2");
};

hello_2().then(console.log);

// rewriting promise code with async await
