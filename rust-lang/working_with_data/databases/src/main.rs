use postgres;
use postgres::{Connection, TlsMode, Error};
use postgres::types::FromSql;

#[derive(Debug)]
struct Weather {
    id: i32,
    month: String,
    normal: f32,
    warmest: f32,
    coldest: f32
}

fn main() -> Result<(), Error> {
    let conn = Connection::connect("postgresql://postgres:postgres@localhost:5432/postgres",
                                    TlsMode::None)?;

     conn.execute("CREATE TABLE IF NOT EXISTS weather (
                    id              SERIAL PRIMARY KEY,
                    month           VARCHAR NOT NULL,
                    normal          FLOAT NOT NULL,
                    warmest         FLOAT NOT NULL,
                    coldest         FLOAT NOT NULL
                  )", &[])?;
    let weathers = vec![
        ("January", 21.3, 27.3, 15.1),
        ("February", 23.6, 30.1, 17.0),
        ("March", 26.1, 32.7, 19.5),
        ("April", 28.0, 34.2, 21.8),
        ("May", 27.4, 33.2, 21.4),
        ("June", 24.6, 29.2, 20.1),
        ("July", 23.9, 28.1, 19.7),
        ("August", 23.5, 27.4, 19.5),
        ("September", 23.9, 28.2, 19.6),
        ("October", 23.7, 28.0, 19.3),
        ("November", 22.2, 27.0, 17.5),
        ("December", 21.1, 26.2, 16.0)
    ];

    for weather in &weathers {
        conn.execute("INSERT INTO weather (month, normal, warmest, coldest) VALUES ($1, $2, $3, $4)",
                 &[&weather.0, &weather.1, &weather.2, &weather.3])?;
    }

    for row in &conn.query("SELECT id, month, normal, warmest, coldest FROM weather", &[])? {
        // let weather = Weather {
        //     id: row.get(0),
        //     month: row.get(1),
        //     normal: FromSql::Into(row.get(2)),
        //     warmest: row.get(3),
        //     coldest: row.get(4)
        // };
        // println!("{:?}", weather);
        let x: i16 = row.get(0).into();
        println!("{:?}", x);
    }

    Ok(())
}