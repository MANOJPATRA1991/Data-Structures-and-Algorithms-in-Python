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

    def insert_left(self, new_node):
        """
        Inserts a new node as the left child of the root
        Args:
            new_node(any): The value to insert
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, new_node):
        """
        Inserts a new node as the right child of the root
        Args:
            new_node(any): The value to insert
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        """
        Get the right child of the root
        """
        return self.rightChild

    def get_left_child(self):
        """
        Get the left child of the root
        """
        return self.leftChild

    def set_root_val(self, obj):
        """
        Set new value for the root
        """
        self.key = obj

    def get_root_val(self):
        """
        Get the value of the root
        """
        return self.key


# r = BinaryTree('a')
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left('b')
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right('c')
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val('hello')
# print(r.get_right_child().get_root_val())
