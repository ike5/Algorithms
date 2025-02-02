class Node:
    """
    A Node class for a Binary Search Tree (BST).
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.data})"

    def insert(self, tree, node):
        if tree.root is None:

            pass