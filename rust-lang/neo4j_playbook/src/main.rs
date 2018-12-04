extern crate rusted_cypher;

use rusted_cypher::GraphClient;

const URI: &'static str = "http://127.0.0.1:7474/db/data";

fn main() {
    let graph = GraphClient::connect(URI).unwrap();
    let mut query = graph.query();

    let statement = "CREATE (n:LANG { name: 'Rust', level: 'low', safe: true })";
    query.add_statement(statement);

    let statement = "CREATE (n:LANG { name: 'C++', level: 'low', safe: true })";
    query.add_statement(statement);

    query.send().unwrap();

    graph.exec(
        "CREATE (n:LANG { name: 'Python', level: 'high', safe: true })")
        .unwrap();
    
    let result = graph.exec(
        "MATCH (n:LANG) RETURN n.name, n.level, n.safe")
        .unwrap();

    assert_eq!(result.data.len(), 3);

    for row in result.rows() {
        let name: String = row.get("n.name").unwrap();
        let level: String = row.get("n.level").unwrap();
        let safeness: bool = row.get("n.safe").unwrap();
        println!("name: {}, level: {}, safe: {}", name, level, safeness);
    }

    graph.exec("MATCH (n:LANG) DELETE n").unwrap();
}
