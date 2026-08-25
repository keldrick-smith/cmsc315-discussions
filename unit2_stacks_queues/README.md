# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation

I created a stack using a Python list and implemented methods to push, pop, peek, and check whether the stack was empty. I used browser history as the stack scenario. Pages were added to the stack and then removed in reverse order, which demonstrated LIFO behavior because the most recently visited page was removed first.

I created a queue using `collections.deque` and implemented methods to enqueue, dequeue, view the front item, and check whether the queue was empty. I used an IT support ticket system as the queue scenario. Tickets were added in the order they were received and processed from the front of the queue, which demonstrated FIFO behavior.
As more items were added, both structures required more memory because each additional value had to be stored. The amount of memory used increased as the number of stored items increased.

# Testing and Edge Cases

I tested popping and peeking from an empty stack and confirmed that both returned `None`. I also created a stack with one item, removed it, and verified that the stack became empty. 

For the queue, I tested dequeuing and checking the front of an empty queue and confirmed that both returned `None`. I also created a queue with one item, removed it, and verified that the queue became empty. These tests helped confirm that the stack and queue handled empty and single-item conditions correctly.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
