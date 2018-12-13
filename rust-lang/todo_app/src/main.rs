#[macro_use]
extern crate yew;

use yew::html::*;
use yew::app::App;
use yew::prelude::*;

struct Model {
    input: String,
    todos: Vec<String>,
}

enum Msg {
    Add,
    Update(String),
    Remove(usize),
    RemoveAll,
    Nothing,
}

impl Component for Model {
    type Message = Msg;
    type Properties = ();

    fn create(_: Self::Properties, _: ComponentLink<Self>) -> Self {
        Model {
            todos: vec![],
            input: "".to_string(),
        }
    }

    fn update(&mut self, msg: Self::Message) -> ShouldRender {
        match msg {
            Msg::Add => {
                let s = self.input.clone();
                self.todos.push(s);
                self.input = "".to_string();
            }
            Msg::Update(s) => {
                self.input = s;
            }
            Msg::Remove(index) => {
                self.todos.remove(index);
            }
            Msg::RemoveAll => {
                self.todos = vec![];
            }
            Msg::Nothing => { }
        }
        true
    }
}

impl Renderable<Model> for Model {
    fn view(&self) -> Html<Self> {
        let view_todo = |(i, todo): (usize, &String)| {
            html! {
                <li>
                    { format!("{} |", &todo) }
                    <button onclick = |_| Msg::Remove(i), >{"remove"}</button>
                </li>
            }
        };
        html! {
            <div>
                <h1>{"Todo App"}</h1>
                <input
                    placeholder="do it",
                    value=&self.input,
                    oninput=|e| Msg::Update(e.value),
                    onkeypress=|e| {
                        if e.key() == "Enter" {Msg::Add} else {Msg::Nothing}
                    },
                    />
                <p>{&self.input}</p>
            </div>
            <div>
                <button onclick=|_| Msg::RemoveAll, >
                    {"Delete all todos"}
                </button>
            </div>
            <div>
                <ul>
                    { for self.todos.iter().enumerate().map(view_todo) }
                </ul>
            </div>
        }
    }
}


fn main() {
    yew::initialize();
    App::<Model>::new().mount_to_body();
    yew::run_loop();
}
