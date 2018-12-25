extern crate smart_open as sm;

#[cfg(test)]
mod tests {
    #[test]
    fn test_gzip_file() {
        // assert_eq!(sm::smart_open("/Users/joydeep/thinking/programming-languages/rust-lang/smart-open/foo.txt").unwrap(), "Hello, world!");
        assert_eq!(sm::smart_open("tests/foo.txt").unwrap(), "Hello, world!");
    }

    #[test]
    #[should_panic(expected = r#"No such file or directory"#)]
    fn test_gzip_file_invalidfile() {
        let _ = sm::smart_open("somefile");
    }
}