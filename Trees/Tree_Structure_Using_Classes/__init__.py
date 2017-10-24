class BinaryTree:
    """
    Creates a Binary Tree with a root, left child and
    right child.
    Attributes:
        rootObj(any): The value of the root of the tree
        leftChild(BinaryTree): The left child of the tree
        rightChild(BinaryTree): The right child of the tree
    """    
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        Inserts a new node as the left child of the root
        Args:
            newNode(any): The value to insert
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """
        Inserts a new node as the right child of the root
        Args:
            newNode(any): The value to insert
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """
        Get the right child of the root
        """
        return self.rightChild

    def getLeftChild(self):
        """
        Get the left child of the root
        """
        return self.leftChild

    def setRootVal(self, obj):
        """
        Set new value for the root
        """
        self.key = obj

    def getRootVal(self):
        """
        Get the value of the root
        """
        return self.key


# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())
