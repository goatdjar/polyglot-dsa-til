from dsa_utils import binary_search

def main():
    sorted_data = [2, 5, 7, 13, 21, 42, 64, 89]
    target = 42

    idx = binary_search(sorted_data, target)
    print(f"Dataset: {sorted_data}")
    print(f"Target {target} found at index: {idx}")

if __name__ == "__main__":
    main()
