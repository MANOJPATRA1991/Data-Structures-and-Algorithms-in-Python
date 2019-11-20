from Trees.Tree_Structure_Using_Classes import BinaryTree


def pre_order(tree):
    if tree:
        # Visit root
        print(tree.get_root_val())
        # Traverse left subtree
        pre_order(tree.get_left_child())
        # Traverse right subtree
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree:
        # Traverse left subtree
        post_order(tree.get_left_child())
        # Traverse right subtree
        post_order(tree.get_right_child())
        # Visit root
        print(tree.get_root_val())


def in_order(tree):
    if tree:
        # Traverse left subtree
        in_order(tree.get_left_child())
        # Visit root
        print(tree.get_root_val())
        # Traverse right subtree
        in_order(tree.get_right_child())
