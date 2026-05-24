from dsa_utils.sorting import quick_sort, merge_sort

def main():
    unsorted_data = [42, 13, 7, 89, 21, 5, 64, 13]
    print(f"Original Array: {unsorted_data}\n")

    # Verify Quick Sort
    q_sorted = quick_sort(unsorted_data)
    print(f"Quick Sorted:   {q_sorted}")

    # Verify Merge Sort
    m_sorted = merge_sort(unsorted_data)
    print(f"Merge Sorted:   {m_sorted}")

if __name__ == "__main__":
    main()
