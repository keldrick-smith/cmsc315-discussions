# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation

I created a linear search that checked each value in the list from beginning to end until the target was found. If the target was found, the program returned its index. If the value was not in the list, it returned `-1`. Linear search had O(n) time complexity because in the worst case it may need to check every value in the list.

I also created a binary search that worked on a sorted list. The search checked the middle value and then removed half of the remaining search area depending on whether the target was higher or lower. This process continued until the target was found or there were no values left to search. Binary search had O(log n) time complexity because the search area was reduced by half each time.

A real-world example of these search methods would be searching through medical records for a specific patient. If the records were not sorted, linear search could check each record one at a time until the correct patient was found. If the records were sorted by patient ID, binary search could find the patient faster by repeatedly cutting the remaining search area in half.

## Testing and Edge Cases

I tested both search algorithms on a small sorted dataset and searched for a value that existed and one that did not. Both searches returned the correct index for the value that was found and returned `-1` for the value that was not in the list.

I also tested both algorithms on a much larger dataset. Both searches returned the same index, but binary search was more efficient because it did not need to check each value one at a time.

For the edge cases, I tested searching an empty list and confirmed that both algorithms returned `-1`. I also tested searching for a value at the last position in the list and confirmed that both algorithms returned the correct index.

## Discussion Board Reflection

While completing this assignment, I learned more about how linear search and binary search work and why the way data is organized matters. Linear search checks each value one at a time, while binary search works with sorted data and keeps cutting the search area in half. I also got more practice working with time complexity and understanding why linear search is O(n) and binary search is O(log n).

One challenge was understanding why binary search cannot just be used on any list. I got past that by thinking about how the middle value only helps if the data is already sorted. Without that order, there would be no way to know which half should be removed.

A real-world example would be searching medical records for a specific patient. If the records were unsorted, linear search would make more sense because each record could be checked until the patient was found. If the records were sorted by patient ID, binary search would be faster, especially with a large number of records. The tradeoff is that binary search is faster, but the data has to already be organized first.

