# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation

The program implemented a Binary Search Tree using a `Node` class and a `BST` class. Each node stored a value and references to its left and right children. The `insert()` function used a recursive helper method to place values in the correct position. Values smaller than the current node were placed in the left subtree, while larger values were placed in the right subtree.

For the real-world example, I used ASVAB scores as the values stored in the BST. The scores `[65, 42, 78, 31, 55, 72, 91]` were inserted into the tree. The `search()` function used recursion to locate a score by comparing it to the current node and then continuing to either the left or right subtree.

The `inorder()` function performed an in-order traversal by visiting the left subtree, the current node, and then the right subtree. This returned the ASVAB scores in ascending order, which demonstrated how a BST can organize numerical data efficiently.

## Testing and Edge Cases

I tested the BST by inserting multiple ASVAB scores that created both left and right subtrees. I performed an in-order traversal and confirmed that the scores were returned in ascending order.

For searching, I tested scores that existed in the tree and confirmed that the function returned `True`. I also searched for scores that were not in the tree and confirmed that the function returned `False`.

The edge-case tests included performing an in-order traversal on an empty tree, searching for a score in an empty tree, and attempting to insert a duplicate ASVAB score. The empty-tree traversal returned an empty list, the empty-tree search returned `False`, and the duplicate score was ignored because the BST only inserted values that were strictly smaller or larger than the current node.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.