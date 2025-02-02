class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"Node Key ({self.key})"
