use dsa_core::searching::binary_search;

fn main() {
    let sorted_data = vec!["apple", "banana", "cherry", "dragonfruit", "elderberry"];
    let target = "dragonfruit";

    match binary_search(&sorted_data, &target) {
        Some(index) => println!("Found '{}' at array index [{}]", target, index),
        None => println!("Element '{}' not found in dataset.", target),
    }
}
