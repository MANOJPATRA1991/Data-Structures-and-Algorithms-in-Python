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
        # Else make the new node the root of the tree
        else:
            self.root = TreeNode(key, val)
        # Increment size by one
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        """
        Helper function to insert tree node in BST
        Args:
            key: key of the tree node
            val: payload of the tree node
            current_node: the TreeNode at which to insert
        Returns:
        """
        # If key is less than current node's key,
        # insert in left subtree
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val, parent=current_node)
        # If key is greater than current node's key,
        # insert in right subtree
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = TreeNode(key, val, parent=current_node)

    def __setitem__(self, k, v):
        """
        Creates a new node with key and value, and inserts the node
        at the correct location in the tree
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
            # If we find the node, return the payload
            if result:
                return result.payload
            else:
                return None
        # Return None if root doesn't exist
        else:
            return None

    def _get(self, key, current_node):
        """
        Helper function to get value for a given key
        Args:
            key: the key to search for in the BST
            current_node: the TreeNode where to begin the search
        Returns:
            The value for the given key if it exists
        """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

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
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                # Remove the node
                self._remove(node_to_remove)
                # Decrement size of the tree
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def _remove(self, current_node):
        """
        Performs the removal of a node from the BST
        Args:
            current_node: the TreeNode to remove
        """
        # If current node is a leaf node
        if current_node.is_leaf():
            if current_node == current_node.parent.leftChild:
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        # If current node has both children
        elif current_node.has_both_children():
            # find successor to take place of node to delete
            successor = current_node.find_successor()
            # remove successor from the tree
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload
        # If current node has only one child
        else:
            # If child is on the left
            if current_node.has_left_child():
                # Connect current node's left child and current node's parent
                if current_node.is_left_child():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.leftChild
                # Connect current node's left child and current node's parent
                elif current_node.is_right_child():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.leftChild
                # If current node is the root node, replace node's data
                else:
                    current_node.replace_node_data(
                        current_node.leftChild.key,
                        current_node.leftChild.payload,
                        current_node.leftChild.leftChild,
                        current_node.leftChild.rightChild)
            # If child is on the right
            else:
                # Connect current node's right child and current node's parent
                if current_node.is_left_child():
                    current_node.rightChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.rightChild
                # Connect current node's right child and current node's parent
                elif current_node.is_right_child():
                    current_node.rightChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.rightChild
                # If current node is the root node, replace the node's data
                else:
                    current_node.replace_node_data(
                        current_node.rightChild.key,
                        current_node.rightChild.payload,
                        current_node.rightChild.leftChild,
                        current_node.rightChild.rightChild)

    def __delitem__(self, key):
        """
        Delete a node from the tree
        Args:
            key: Key of the node
        """
        self.delete(key)


class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        """
        Args:
            key: Key for the node
            val: Payload of the node
            left: Left child of the node
            right: Right child of the node
            parent: Parent of the node
        """
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.rightChild or self.leftChild)

    def has_any_children(self):
        return self.rightChild or self.leftChild

    def has_both_children(self):
        return self.rightChild and self.leftChild

    def replace_node_data(self, key, value, lc, rc):
        """
        Replace node's data
        Args:
            key: Key of the node
            value: Payload of the node
            lc: Left child of the node
            rc: Right child of the node
        """
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.has_left_child():
            self.leftChild.parent = self
        if self.has_right_child():
            self.rightChild.parent = self

    def find_successor(self):
        """
        Find a successor to replace the node to delete
        Returns:
            Successor to deleted node
        """
        successor = None
        # If the node has a right child, then the successor is
        # the smallest key in the right subtree.
        if self.has_right_child():
            successor = self.rightChild.find_min()
        else:
            # If the node has no right child
            if self.parent:
                # If the node is the left child of
                # its parent, then the parent is the successor.
                if self.is_left_child():
                    successor = self.parent
                # If the node is the right child of its parent,
                # then successor to this node is the successor
                # of its parent, excluding this node
                else:
                    self.parent.rightChild = None
                    successor = self.parent.find_successor()
                    self.parent.rightChild = self
        return successor

    def find_min(self):
        """
        Find node with minimum key
        """
        current = self
        # minimum key is the deepest node on the left
        while current.has_left_child():
            current = current.leftChild
        return current

    def splice_out(self):
        """
        Removes the successor to a node from the tree
        """
        if self.is_leaf():
            if self.is_left_child():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.leftChild:
                    yield elem
        yield self.key
        if self.has_right_child():
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
