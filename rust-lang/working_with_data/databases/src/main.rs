// use postgres;
// use postgres::{Connection, TlsMode, Error};

// #[derive(Debug)]
// struct Weather {
//     id: i32,
//     month: String,
//     normal: f64,
//     warmest: f64,
//     coldest: f64
// }

// fn main() -> Result<(), Error> {
//     let conn = Connection::connect("postgresql://postgres:postgres@localhost:5432/postgres",
//                                     TlsMode::None)?;

//      conn.execute("CREATE TABLE IF NOT EXISTS weather (
//                     id              SERIAL PRIMARY KEY,
//                     month           VARCHAR NOT NULL,
//                     normal          DOUBLE PRECISION NOT NULL,
//                     warmest         DOUBLE PRECISION NOT NULL,
//                     coldest         DOUBLE PRECISION NOT NULL
//                   )", &[])?;
//     let weathers = vec![
//         ("January", 21.3, 27.3, 15.1),
//         ("February", 23.6, 30.1, 17.0),
//         ("March", 26.1, 32.7, 19.5),
//         ("April", 28.0, 34.2, 21.8),
//         ("May", 27.4, 33.2, 21.4),
//         ("June", 24.6, 29.2, 20.1),
//         ("July", 23.9, 28.1, 19.7),
//         ("August", 23.5, 27.4, 19.5),
//         ("September", 23.9, 28.2, 19.6),
//         ("October", 23.7, 28.0, 19.3),
//         ("November", 22.2, 27.0, 17.5),
//         ("December", 21.1, 26.2, 16.0)
//     ];

//     for weather in &weathers {
//         conn.execute("INSERT INTO weather (month, normal, warmest, coldest) VALUES ($1, $2, $3, $4)",
//                  &[&weather.0, &weather.1, &weather.2, &weather.3])?;
//     }

//     // print and see if they are correct
//     for row in &conn.query("SELECT id, month, normal, warmest, coldest FROM weather", &[])? {
//         let weather = Weather {
//             id: row.get(0),
//             month: row.get(1),
//             normal: row.get(2),
//             warmest: row.get(3),
//             coldest: row.get(4)
//         };
//         println!("{:?}", weather);
//     }

//     // get the average value
//     for row in &conn.query("SELECT AVG(warmest) FROM weather;", &[])? {
//         let x: f64 = row.get(0);
//         println!("{:?}", x);
//     }

//     Ok(())
// }

// try the movielens dataset http://gree2.github.io/database/viz/2016/12/31/import-movielens-data-into-neo4j-container

use rusted_cypher;
use rusted_cypher::{GraphClient, Statement, GraphError};

fn main() -> Result<(), GraphError> {
    // let graph = GraphClient::connect(
    //     "http://neo4j:neo4j@localhost:7474/db/data");
    let graph = GraphClient::connect(
        "http://localhost:7474/db/data")?;

    let mut query = graph.query();

    // // Statement implements From<&str>
    // query.add_statement(
    //     "CREATE (n:LANG { name: 'Rust', level: 'low', safe: true })");

    // let statement = Statement::new(
    //     "CREATE (n:LANG { name: 'C++', level: 'low', safe: {safeness} })")
    //     .with_param("safeness", false)?;

    // query.add_statement(statement);

    // query.send()?;

    // graph.exec(
    //     "CREATE (n:LANG { name: 'Python', level: 'high', safe: true })")?;

    // let result = graph.exec(
    //     "MATCH (n:LANG) RETURN n.name, n.level, n.safe")?;

    // assert_eq!(result.data.len(), 3);

    // for row in result.rows() {
    //     let name: String = row.get("n.name")?;
    //     let level: String = row.get("n.level")?;
    //     let safeness: bool = row.get("n.safe")?;
    //     println!("name: {}, level: {}, safe: {}", name, level, safeness);
    // }

    // graph.exec("MATCH (n:LANG) DELETE n")?;

    let statement1 = Statement::new(
        "CREATE CONSTRAINT ON (m:Movie) ASSERT m.id IS UNIQUE;")?;
    let statement2 = Statement::new(
        " CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;"
    )?;
    let statement3 = Statement::new(
        " CREATE CONSTRAINT ON (g:Genre) ASSERT g.name IS UNIQUE;"
    )?;



    query.add_statement(statement1);
    query.add_statement(statement2);
    query.add_statement(statement3);

    query.send()?;

    Ok(())
}
