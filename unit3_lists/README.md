# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Implementation

The program implemented three main list operations: insertion, deletion, and searching. The `insert_at()` function used `insert()` method to place a value at a selected index. I tested insertion at the beginning, middle, and end of the playlist so I could see how the list changed as elements were added.
The `delete_at()` function checked whether the index was valid before it removed an item. If the index existed, `pop()` removed and returned the selected song. If the index was invalid, the function returned `None` instead of causing `IndexError`.
The `search_value()` function used a linear search that checked each item until a match was found. It returned the index of an existing value and returned `-1` when the value was not found. I used song titles in a playlist as the real-world example because playlists depend on ordered data and allow items to be added, removed, and searched.

## Testing and Edge Cases

I tested insertion at the beginning, middle, and end of the playlist and displayed the updated list after each operation. I also tested deletion from the beginning, middle, and end and displayed both the removed value and the remaining songs.
For searching, I tested `"GG"` as an existing song and confirmed that the search returned index `0`. I also searched for a missing value and confirmed that the function returned `-1`.
The edge-case tests included deleting with an invalid index, deleting from an empty list, inserting into an empty list, and searching for a value that was not present. Invalid deletion and deletion from an empty list both returned `None`, while the empty list successfully accepted `"GG"` as its first item. The program completed all tests successfully with exit code `0`.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
