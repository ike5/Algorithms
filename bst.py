def bst_remove(tree, key):
    parent = None
    current_node = tree.root

    while current_node is not None:
        # check if current_node has an equal key
        if current_node.key == key:
            if current_node.left is None and current_node.right is None:
                # remove leaf
                if parent is None:  # is root
                    tree.root = None
                elif parent.left is current_node:
                    parent.left = None
                else:
                    parent.right = None
                return True  # Node found and removed

            elif current_node.right is None:
                # remove node with only left child
                if parent is None:  # is root
                    tree.root = current_node.left
                elif parent.left == current_node.left:
                    parent.left = current_node.left
                else:
                    parent.right = current_node.left
                return True  # Node found and removed
            else:
                # Remove node with two children
                # Find successor (leftmost child of right subtree)
                successor = current_node.right
                while successor.left is not None:
                    successor = successor.left

                # Copy successor's key to current node
                current_node.key = successor.key
                parent = current_node

                # Reassign current_node and key so that loop continues with new key
                current_node = current_node.right
                key = successor.key

        elif current_node.key < key:
            # search right
            parent = current_node
            current_node = current_node.right
        else:
            # search left
            parent = current_node
            current_node = current_node.left
    return False
