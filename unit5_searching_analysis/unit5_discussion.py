"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each value one at a time from beginning to end.
    # In the worst case, it may have to check every value in the list.
    # Because the number of comparisons can grow with the size of the list,
    # linear search has O(n) time complexity.

    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2

        if lst[middle] == target:
            return middle

        # If the target is larger than the middle value,
        # the entire left half can be eliminated.
        elif target > lst[middle]:
            low = middle + 1

        # If the target is smaller than the middle value,
        # the entire right half can be eliminated.
        else:
            high = middle - 1

        # Each iteration removes about half of the remaining search area,
        # which gives binary search O(log n) time complexity.

    return -1


def main():

    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_dataset = [10, 20, 30, 40, 50]

    # 30 exists in the list, so both searches should return index 2.
    print("Linear search for 30:", linear_search(small_dataset, 30))
    print("Binary search for 30:", binary_search(small_dataset, 30))

    # 35 is not in the list, so both searches should return -1.
    print("Linear search for 35:", linear_search(small_dataset, 35))
    print("Binary search for 35:", binary_search(small_dataset, 35))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_dataset = list(range(1, 10001))
    target = 9999

    print("Linear search for 9999:", linear_search(large_dataset, target))
    print("Binary search for 9999:", binary_search(large_dataset, target))

    # Both searches return the same index when the value is found.
    # However, linear search may check thousands of values before finding
    # the target. Binary search repeatedly cuts the remaining search area
    # in half, so it requires far fewer comparisons as the dataset grows.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

      # Edge case 1: Searching an empty list.
    # Since there are no values to search, both algorithms return -1.
    empty_list = []
    print("Linear search empty list:", linear_search(empty_list, 10))
    print("Binary search empty list:", binary_search(empty_list, 10))

    # Edge case 2: Searching for the last value in a list.
    # Both searches should successfully return index 4.
    edge_dataset = [10, 20, 30, 40, 50]
    print("Linear search last value:", linear_search(edge_dataset, 50))
    print("Binary search last value:", binary_search(edge_dataset, 50))

if __name__ == "__main__":
    main()