"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # insert() places the value at the specified index.
    # Elements at and after that position shift one position to the right.
    # Inserting near the beginning or middle may require more shifting,
    # while inserting at the end usually requires less work.
    lst.insert(index, value)

def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validate the index before removing an item to prevent an IndexError.
    # Safe deletion is important because users may provide an invalid position.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes and returns the value stored at the selected index.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because each value is checked in order
    # from the beginning of the list until a match is found.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Return -1 when the value does not appear anywhere in the list.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    playlist = ["GG", "SICKO", "FERRARI"]
    print("Original list:", playlist)

    # Insert at the beginning of the list.
    insert_at(playlist, 0, "bada bing, bada bØØm (feat. Tezzus)")
    print("After beginning insertion:", playlist)

    # Insert into the middle of the list.
    insert_at(playlist, 2, "FØURS (feat. Young Thug)")
    print("After middle insertion:", playlist)

    # Insert at the end using the current list length as the index.
    insert_at(playlist, len(playlist), "MAN ØN THE MØØN")
    print("After end insertion:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first item in the list.
    removed = delete_at(playlist, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", playlist)

    # Remove an item from the middle.
    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", playlist)

    # Remove the final item in the list.
    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from end:", removed)
    print("Updated list:", playlist)


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a song that currently exists in the list.
    result = search_value(playlist, "GG")
    print("Index of 'GG':", result)

    # Search for a song that is not stored in the list.
    result = search_value(playlist, "Missing Song")
    print("Index of missing song:", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Attempt to delete using an invalid index.
    invalid_delete = delete_at(playlist, 50)
    print("Invalid index deletion:", invalid_delete)

    # Edge case 2: Attempt to delete from an empty list.
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print("Delete from empty list:", empty_delete)

    # Edge case 3: Insert into an empty list.
    insert_at(empty_list, 0, "GG")
    print("Insert into empty list:", empty_list)

    # Edge case 4: Search for a value that does not exist.
    missing_search = search_value(playlist, "Not Here")
    print("Missing value search:", missing_search)


if __name__ == "__main__":
    main()