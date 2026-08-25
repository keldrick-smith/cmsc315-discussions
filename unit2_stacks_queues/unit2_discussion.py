"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque

class Stack:
    def __init__(self):
        # A Python list is used to store stack values.
        self.items = []

    def push(self, value):
        # The newest value is added to the top and will be removed first.
        self.items.append(value)

    def pop(self):
        # Remove and return the most recently added value.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # Return the top value without removing it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack has no values.
        return len(self.items) == 0

class Queue:
    def __init__(self):
        # deque is used for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # New values are added to the back while older values stay at the front.
        self.items.append(value)

    def dequeue(self):
        # Remove and return the value from the front of the queue.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # Return the front value without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Return True if the queue has no values.
        return len(self.items) == 0

def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    browser_history = Stack()

    browser_history.push("Home")
    browser_history.push("Profile")
    browser_history.push("Settings")
    browser_history.push("Help")

    print("Browser pages were added to the stack.")
    print("Top page:", browser_history.peek())

    print("Going back through pages in LIFO order:")
    while not browser_history.is_empty():
        print(browser_history.pop())

    print("Pop on empty stack:", browser_history.pop())
    print("Peek on empty stack:", browser_history.peek())

    single_stack = Stack()
    single_stack.push("Home")
    single_stack.pop()
    print("Single-item stack is empty:", single_stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    support_queue = Queue()

    support_queue.enqueue("Password reset")
    support_queue.enqueue("Printer issue")
    support_queue.enqueue("Software update")
    support_queue.enqueue("Network issue")

    print("Support tickets were added to the queue.")
    print("Next ticket:", support_queue.front())

    print("Processing tickets in FIFO order:")
    while not support_queue.is_empty():
        print(support_queue.dequeue())

    print("Dequeue on empty queue:", support_queue.dequeue())
    print("Front on empty queue:", support_queue.front())

    single_queue = Queue()
    single_queue.enqueue("Account unlock")
    single_queue.dequeue()
    print("Single-item queue is empty:", single_queue.is_empty())


if __name__ == "__main__":
    main()