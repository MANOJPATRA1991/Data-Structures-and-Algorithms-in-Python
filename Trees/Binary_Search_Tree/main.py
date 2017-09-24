class BinarySearchTree(object):

    def __init__(self):
        """
        Constructor function to instantiate
        a binary search tree
        """
        self.root = None
        self.size = 0

    def length(self):
        """
        Returns size of binary search tree
        Returns:
            Size of binary search tree
        """
        return self.size

    def __len__(self):
        """
        Returns:
            Size of binary search tree
        """
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """
        Inserts a tree node in the BST
        Args:
             key: key of tree node
             val: payload of tree node
        """
        # If root exists
        if self.root:
            self._put(key, val, self.root)
        # Else make the new tree node the root
        else:
            self.root = TreeNode(key, val)
        # Increment size by one
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        """
        Helper function to insert tree node in BST
        Args:
            key: key of the tree node
            val: payload of the tree node
            currentNode: the TreeNode at which to insert
        Returns:
        """
        # If key is less than current node's key,
        # insert in left subtree
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        # If key is greater than current node's key,
        # insert in right subtree
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        """
        Set new key-value pair
        Args:
            k: key of the tree node
            v: payload of the tree node
        """
        self.put(k, v)

    def get(self, key):
        """
        Get the value for a given key
        Args:
            key: key of the tree node
        Returns:
            Value for the given key if node exists
        """
        # If root exists, search for the node with given key
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.payload
            else:
                return None
        # Return None if root doesn't exist
        else:
            return None

    def _get(self, key, currentNode):
        """
        Helper function to get value for a given key
        Args:
            key: the key to search for in the BST
            currentNode: the TreeNode where to begin the search
        Returns:
            The value for the given key if it exists
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        """
        Get value for a key
        Args:
            key: key of the tree node
        Returns:
            payload of the tree node
        """
        return self.get(key)

    def __contains__(self, key):
        """
        Checks if node with given key is in BST
        Args:
            key: key of the tree node
        Returns:
            Boolean value
        """
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """
        Deletes a node with the specified key
        Args:
            key: key of the node to delete
        """
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, currentNode):
        """
        Performs the removal of a node from the BST
        Args:
            currentNode: the TreeNode to remove
        """
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            # find successor to take place of node to delete
            successor = currentNode.findSuccessor()
            # remove successor from the tree
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)

    def __delitem__(self, key):
        """
        Delete a node from the tree
        Args:
            key: Key of the node
        """
        self.delete(key)


class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        """
        Find a successor to replace the node to delete
        Returns:
            Successor to deleted node
        """
        successor = None
        # If the node has a right child, then the successor is
        # the smallest key in the right subtree.
        if self.hasRightChild():
            successor = self.rightChild.findMin()
        else:
            # If the node has no right child
            if self.parent:
                # If the node is the left child of
                # its parent, then the parent is the successor.
                if self.isLeftChild():
                    successor = self.parent
                # If the node is the right child of its parent,
                # then successor to this node is the successor
                # of its parent, excluding this node
                else:
                    self.parent.rightChild = None
                    successor = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return successor

    def findMin(self):
        """
        Find node with minimum key
        """
        current = self
        # minimum key is the deepest node on the left
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        """
        Removes the successor to a node from the tree
        """
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.rightChild:
                yield elem


mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"

print(mytree[6])
print(mytree[2])
del mytree[3]
print(mytree[3])
