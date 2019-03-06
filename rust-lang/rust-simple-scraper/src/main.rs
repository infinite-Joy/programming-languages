use reqwest;
//use select;
use select::document::Document;
use select::predicate::{Class, Name, Predicate};
use scraper::{Selector, Html};

fn main() -> Result<(), Box<std::error::Error>> {
    let mut resp = reqwest::get(
        "https://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/ntpc/NTP")?;
    assert!(resp.status().is_success());

    let body = resp.text().unwrap();
    let fragment = Html::parse_document(&body);
    let stories = Selector::parse("#Bse_Prc_tick > strong:nth-child(1)").unwrap();

    for price in fragment.select(&stories) {
        let price_txt = price.text().collect::<Vec<_>>();
        println!("{:?}", price_txt);
    }

    Ok(())
}

