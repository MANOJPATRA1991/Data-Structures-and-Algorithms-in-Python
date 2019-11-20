from Trees.Binary_Search_Tree.main import BinarySearchTree, TreeNode


class AVLTree(BinarySearchTree):
    def _put(self, key, val, currentNode):
        """
        Insert a new node in the binary search tree
        """
        # If key is less than the current node, it should go in left side
        if key < currentNode.key:
            
            # If current node has left child, the new node should go in the left subtree
            if currentNode.has_left_child():
                self._put(key, val, currentNode.leftChild)    
            else:
                # Otherwise the new node is the left child of the current node
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                
                # Update balance factor of current node and its ancestors as required
                self.update_balance(currentNode.leftChild)
                
        # If key is greater than the current node, it should go in right side        
        else:
            
            # If current node has right child, the new node should go in the right subtree
            if currentNode.has_right_child():
                self._put(key, val, currentNode.rightChild)
            else:
                # Otherwise the new node is the right child of the current node
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                
                # Update balance factor of current node and its ancestors as required
                self.update_balance(currentNode.rightChild)

    def update_balance(self, node):
        """
        Update balance factors of all nodes as required
        A node is said to be balanced if it has a balance factor of either 1, -1 or 0
        """
        # If the current node is out of balance, re-balance it and return
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.re_balance(node)
            return
        
        # If current node is balanced, update balance factor of parent
        if node.parent is not None:
            
            # If current node is the left child,
            # increment it's parent's balance factor by 1
            if node.is_left_child():
                node.parent.balanceFactor = node.parent.balanceFactor + 1
                
            # If current node is the right child,
            # decrement it's parent's balance factor by 1    
            elif node.is_right_child():
                node.parent.balanceFactor = node.parent.balanceFactor - 1
                
            # If balance factor of parent after update is not zero,
            # call update_balance on the parent
            if node.parent.balanceFactor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rot_root):
        """
        Rotate tree left
        """
        new_root = rot_root.rightChild
        rot_root.rightChild = new_root.leftChild
        if new_root.leftChild is not None:
            new_root.leftChild.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.leftChild = new_root
            else:
                rot_root.parent.rightChild = new_root
        new_root.leftChild = rot_root
        rot_root.parent = new_root
        rot_root.balanceFactor = rot_root.balanceFactor + \
                                 1 - min(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor + \
            1 + max(rot_root.balanceFactor, 0)

    def rotate_right(self, rot_root):
        new_root = rot_root.leftChild
        rot_root.leftChild = new_root.rightChild
        if new_root.rightChild is not None:
            new_root.rightChild.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.leftChild = new_root
            else:
                rot_root.parent.rightChild = new_root
        new_root.rightChild = rot_root
        rot_root.parent = new_root
        rot_root.balanceFactor = rot_root.balanceFactor - \
                                 1 - max(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor - \
            1 - min(rot_root.balanceFactor, 0)

    def re_balance(self, node):
        # Check if tree is right-heavy
        if node.balanceFactor < 0:
            
            # Check if right child is left-heavy
            if node.rightChild.balanceFactor > 0:
                # 1. Rotate node's right tree to right
                self.rotate_right(node.rightChild)
                # 2. Rotate tree with current node as root to left
                self.rotate_left(node)
                
            # If right child is right-heavy
            else:
                # 1. Rotate tree with current node as root to left 
                self.rotate_left(node)
        
        # Check if tree is left-heavy
        elif node.balanceFactor > 0:
            
            # Check if left child is right-heavy
            if node.leftChild.balanceFactor < 0:
                # 1. Rotate node's left tree to left
                self.rotate_left(node.leftChild)
                # 2. Rotate tree with current node as root to right
                self.rotate_right(node)
            
            # If left child is left-heavy
            else:
                # 1. Rotate tree with current node as root to right
                self.rotate_right(node)
