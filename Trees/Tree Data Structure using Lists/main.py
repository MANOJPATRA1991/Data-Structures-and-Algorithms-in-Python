def BinaryTree(r):
    """
    This function creates a binary tree
    representation using list with the first element as
    the root
    Args:
        r(int/string): The value of root of the tree
    Returns:
        List: A list with first element being
            the root
    """
    return [r, [], []]


def insertLeft(root, newBranch):
    """
    Insert a new branch as the left child 
    of the root node in the tree
    Args:
        root(List): The tree in which to insert
        newBranch(int/string): The value to insert
    """
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    """
    Insert a new branch as the right child 
    of the root node in the tree
    Args:
        root(List): The tree in which to insert
        newBranch(int/string): The value to insert
    """
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    """
    Get the root value
    root(List): The Binary Tree list
    """
    return root[0]


def setRootVal(root, newVal):
    """
    Set the root value
    Args: 
        root(List): The binary tree list object
        value(int/string): New value for the root
    """
    root[0] = newVal


def getLeftChild(root):
    """
    Get the left child of the root
    Args: 
        root(List): The binary tree list object
    """    
    return root[1]


def getRightChild(root):
    """
    Get the right child of the root
    Args: 
        root(List): The binary tree list object
    """    
    return root[2]


r = BinaryTree(3)
print(r)
insertLeft(r, 4)
print(r)
insertLeft(r, 5)
print(r)
insertRight(r, 6)
print(r)
insertRight(r, 7)
print(r)

left = getLeftChild(r)
# print(left)

setRootVal(left, 9)
# print(r)
insertLeft(left, 11)
# print(r)
# print(get_right_child(get_right_child(r)))

# OUTPUT:
# [3, [], []]
# [3, [4, [], []], []]
# [3, [5, [4, [], []], []], []]
# [3, [5, [4, [], []], []], [6, [], []]]
# [3, [5, [4, [], []], []], [7, [], [6, [], []]]]