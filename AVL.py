import Node


def avl_tree_update_height(node):
    left_height = -1
    if node.left is not None:
        left_height = node.left.height

    right_height = -1
    if node.right is not None:
        right_height = node.right.height

    node.height = max(left_height, right_height) + 1


def avl_tree_set_child(parent, which_child, child):
    if which_child is not "left" and which_child is not "right":
        return False

    if which_child == "left":
        parent.left = child
    else:
        parent.right = child

    if child is not None:
        child.parent = parent

    avl_tree_update_height(parent)
    return True


def avl_tree_replace_child(parent, current_child, new_child):
    if parent.left == current_child:
        return avl_tree_set_child(parent, "left", new_child)
    elif parent.right == current_child:
        return avl_tree_set_child(parent, "right", new_child)
    return False


def avl_tree_get_balance(node):
    left_height = -1
    if node.left is not None:
        left_height = node.left.height

    right_height = -1
    if node.right is not None:
        right_height = node.right.height

    return left_height - right_height

