use std::cmp::Ordering;

pub fn binary_search<T: Ord>(arr: &[T], target: &T) -> Option<usize> {
    let mut low = 0;
    let mut high = arr.len();

    while low < high {
        let mid = low + (high - low) / 2;
        match arr[mid].cmp(target) {
            Ordering::Equal => return Some(mid),
            Ordering::Greater => high = mid,
            Ordering::Less => low = mid + 1,
        }
    }
    None
}
