from Trees.Tree_Structure_Using_Classes import BinaryTree


def pre_order(tree):
    if tree:
        print(tree.getRootVal())
        pre_order(tree.getLeftChild())
        pre_order(tree.getRightChild())


def post_order(tree):
    if tree:
        post_order(tree.getLeftChild())
        post_order(tree.getRightChild())
        print(tree.getRootVal())


def in_order(tree):
    if tree:
        in_order(tree.getLeftChild())
        print(tree.getRootVal())
        in_order(tree.getRightChild())
