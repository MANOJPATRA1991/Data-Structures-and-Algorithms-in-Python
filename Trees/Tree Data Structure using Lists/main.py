def BinaryTree(r):
    """This function creates a binary tree
    representation using list with the first element as
    the root
    @params: Number"""
    return [r, [], []]


def insertLeft(root, newBranch):
    """Insert a left child newBranch in the tree with root node
    specified by parameter root"""
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    """Insert a right child newBranch in the tree with root node
    specified by parameter root"""
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)

left = getLeftChild(r)
print(left)

setRootVal(left, 9)
print(r)
insertLeft(left, 11)
print(r)
print(getRightChild(getRightChild(r)))
