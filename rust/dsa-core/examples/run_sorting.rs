use dsa_core::sorting::bubble_sort;

fn main() {
    let mut numbers = vec![74, 23, 5, 89, 32, 12];
    println!("Original array: {:?}", numbers);

    bubble_sort(&mut numbers);
    println!("Sorted array: {:?}", numbers);
}
