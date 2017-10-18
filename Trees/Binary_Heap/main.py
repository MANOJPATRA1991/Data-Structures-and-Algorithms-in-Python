class BinHeap:
    """
    HEAP ORDER PROPERTY:
    
    In a heap, for every node x with parent p, 
    the key in p is smaller than or equal to the key in x.
    """
    def __init__(self):
        # zero is the first element to make simple interger division
        # to find index to insert node in
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        """
        **Ensures that the smallest child is always moved up the tree**
        Adjust the binary heap to maintain the heap order property
        """
        # While parent exist
        while i // 2 > 0:
            # If item is less than its parent, 
            # then we can swap the item with its parent. 
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = \
                    self.heap_list[i], self.heap_list[i // 2]
                i = i // 2

    def insert(self, k):
        """
        Insert a new node in the binary heap
        """
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        # call perc_up with the index of the newly added item,
        # i.e., the last item
        self.perc_up(self.current_size)

    def del_min(self):
        """
        Delete min element
        """
        ret_val = self.heap_list[1]
        # Move the last node to make it the new root node
        self.heap_list[1] = self.heap_list[self.current_size]
        # Decrement current size by 1
        self.current_size = self.current_size - 1
        # Remove the last item from the heap_list as it is now moved to the root
        self.heap_list.pop()
        # Call perc_down to ensure that the largest child is always moved down the tree
        self.perc_down(1)
        return ret_val

    def perc_down(self, i):
        """
        **Ensures that the largest child is always moved down the tree**
        Adjust the binary heap after removal of min node by maintaining
        the heap order property
        Args:
            i(int): index of node to percolate down
        """
        # Check if left child exists for current value of i
        while(i * 2) <= self.current_size:
            # Find the index of minimum valued child
            mc = self.min_child(i)
            # Swap if parent value is greater than 
            # minimum child's value
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = \
                    self.heap_list[mc], self.heap_list[i]
            # Make minimum child's index the next value of i
            i = mc

    def min_child(self, i):
        """
        Get the minimum valued child of an element
        Args:
            i(int): Index of parent
        Returns:
            Index of child with minimum value
        """
        # If right child doesn't exist return left child
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, alist):
        """
        Building a heap from a given list
        Args:
            alist: A list from which to build the Binary Heap
        """
        #
        # Starting with a single item => Binary search to find the
        # right place to enter which is O(logn) and shifting of elements
        # which is O(n) => O(nlogn)
        # Starting with an entire list instead of a list with a single item
        # results in O(n) run time instead of O(nlogn)
        #
        self.heap_list = [0] + alist[:]
        # Starting at the middle and working our way back to the root
        i = len(alist) // 2
        self.current_size = len(alist)
        while i > 0:
            # Percolate down until all max values have moved down
            self.perc_down(i)
            i = i - 1


bh = BinHeap()
bh.build_heap([9, 5, 6, 2, 3])

print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
