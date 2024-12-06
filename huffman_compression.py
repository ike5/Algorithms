import heapq
from collections import Counter


# Define Node Classes
class Node:
    def __init__(self, frequency):
        self.frequency = frequency

    def __lt__(self, other):
        # Comparison operator for priority queue (heapq)
        return self.frequency < other.frequency


class LeafNode(Node):
    def __init__(self, frequency, character):
        super().__init__(frequency)
        self.character = character


class InternalNode(Node):
    def __init__(self, frequency, left, right):
        super().__init__(frequency)
        self.left = left
        self.right = right


# Function to Build Character Frequency Table
def BuildCharacterFrequencyTable(inputString):
    return Counter(inputString)


# Function to Build Huffman Tree
def HuffmanBuildTree(inputString):
    # Step 1: Build Frequency Table
    frequency_table = BuildCharacterFrequencyTable(inputString)

    # Step 2: Create Priority Queue of Nodes
    nodes = []
    for char, freq in frequency_table.items():
        heapq.heappush(nodes, LeafNode(freq, char))

    # Step 3: Build the Tree
    while len(nodes) > 1:
        # Remove two nodes with the lowest frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # Create a new internal node with these two nodes as children
        freq_sum = left.frequency + right.frequency
        parent = InternalNode(freq_sum, left, right)

        # Add the new node back to the priority queue
        heapq.heappush(nodes, parent)

    # Step 4: Return the root of the tree
    return heapq.heappop(nodes) if nodes else None


def print_huffman_tree(node, prefix=""):
    """Helper function to print the Huffman tree."""
    if isinstance(node, LeafNode):
        print(f"Character: {node.character}, Frequency: {node.frequency}, Code: {prefix}")
    elif isinstance(node, InternalNode):
        print_huffman_tree(node.left, prefix + "0")
        print_huffman_tree(node.right, prefix + "1")


# Input string
input_string = "BANANAS"

# Build Huffman Tree
tree_root = HuffmanBuildTree(input_string)

# Print the tree
print("Huffman Tree:")
print_huffman_tree(tree_root)
