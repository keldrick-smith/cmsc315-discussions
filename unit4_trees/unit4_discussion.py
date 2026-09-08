"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each node stores one value and starts without children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # An empty BST does not have a root node yet.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # The recursive helper begins at the root.
        # Smaller values move left and larger values move right.

        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If an empty position is reached, create the new node here.
        if node is None:
            return Node(value)

        # Values smaller than the current node belong on the left.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Values larger than the current node belong on the right.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this implementation.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A BST can reduce the search space after each comparison.
        # Instead of checking every node, the search chooses either
        # the left or right subtree based on the value being searched.

        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If the search reaches an empty position, the value is absent.
        if node is None:
            return False

        # If the current node matches, the search is complete.
        if value == node.value:
            return True

        # Smaller values can only exist in the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Larger values can only exist in the right subtree.
        return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # In-order traversal follows left, node, right.
            # Since smaller values are stored on the left and larger
            # values are stored on the right, this produces sorted output.

            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== ASVAB SCORE TREE CONSTRUCTION ===")

    score_tree = BST()

    # These example ASVAB scores create values in both the
    # left and right subtrees of the BST.
    asvab_scores = [65, 42, 78, 31, 55, 72, 91]

    for score in asvab_scores:
        score_tree.insert(score)

    # A BST can reduce the search space after each comparison.
    # If the target score is lower than the current score, the
    # right subtree can be ignored. If it is higher, the left
    # subtree can be ignored.
    print("ASVAB scores inserted:", asvab_scores)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits the left subtree, current node,
    # and right subtree, which returns the ASVAB scores in
    # ascending numerical order.
    print("ASVAB scores in sorted order:", score_tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # These scores were inserted into the tree, so the searches
    # should return True.
    print("Search for score 55:", score_tree.search(55))
    print("Search for score 72:", score_tree.search(72))

    # These scores were not inserted, so the searches
    # should return False.
    print("Search for score 40:", score_tree.search(40))
    print("Search for score 99:", score_tree.search(99))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    empty_score_tree = BST()

    # Traversing an empty BST returns an empty list because
    # no ASVAB scores have been inserted.
    print("Empty score tree traversal:", empty_score_tree.inorder())

    # Searching an empty tree immediately returns False.
    print("Search empty score tree for 65:", empty_score_tree.search(65))

    # Duplicate scores are ignored by this implementation because
    # values are only inserted when they are strictly smaller
    # or larger than the current node.
    score_tree.insert(65)
    print("After attempting duplicate score 65:", score_tree.inorder())

if __name__ == "__main__":
    main()