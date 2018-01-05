from Trees.Binary_Search_Tree.main import BinarySearchTree, TreeNode


class AVLTree(BinarySearchTree):
    def _put(self, key, val, currentNode):
        """
        Insert a new node in the binary search tree
        """
        # If key is less than the current node, it should go in left side
        if key < currentNode.key:
            
            # If current node has left child, the new node should go in the left tree
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)    
            else:
                # Otherwise the new node is the left child of the current node
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                
                # Update balance factor of current node and its ancestors as required
                self.updateBalance(currentNode.leftChild)
                
        # If key is greater than the current node, it should go in right side        
        else:
            
            # If current node has right child, the new node should go in the right tree
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                # Otherwise the new node is the right child of the current node
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                
                # Update balance factor of current node and its ancestors as required
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        """
        Update balance factors of all nodes as required
        A node is said to be balanced if it has a balance factor of either 1, -1 or 0
        """
        # If the current node is out of balance, rebalance it and return
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.reBalance(node)
            return
        
        # If current node is balanced, update balance factor of parent
        if node.parent is not None:
            
            # If current node is the left child,
            # increment it's parent's balance factor by 1
            if node.isLeftChild():
                node.parent.balanceFactor = node.parent.balanceFactor + 1
                
            # If current node is the right child,
            # decrement it's parent's balance factor by 1    
            elif node.isRightChild():
                node.parent.balanceFactor = node.parent.balanceFactor - 1
                
            # If balance factor of parent after update is not zero,
            # call updateBalance on the parent
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        """
        Rotate tree left
        """
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild is not None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
            1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
            1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild is not None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
            1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
            1 + max(rotRoot.balanceFactor, 0)

    def reBalance(self, node):
        # Check if tree is right-heavy
        if node.balanceFactor < 0:
            
            # Check if right child is left-heavy
            if node.rightChild.balanceFactor > 0:
                # 1. Rotate node's right tree to right
                self.rotateRight(node.rightChild)
                # 2. Rotate tree with current node as root to left
                self.rotateLeft(node)
                
            # If right child is not left-heavy    
            else:
                # 1. Rotate tree with current node as root to left 
                self.rotateLeft(node)
        
        # Check if tree is left-heavy
        elif node.balanceFactor > 0:
            
            # Check if left child is right-heavy
            if node.leftChild.balanceFactor < 0:
                # 1. Rotate node's left tree to left
                self.rotateLeft(node.leftChild)
                # 2. Rotate tree with current node as root to right
                self.rotateRight(node)
            
            # If left child is not right-heavy
            else:
                # 1. Rotate tree with current node as root to right
                self.rotateRight(node)
