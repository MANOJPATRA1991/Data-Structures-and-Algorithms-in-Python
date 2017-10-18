class PriorityQueue:
    """
    HEAP ORDER PROPERTY:

    In a heap, for every node x with parent p,
    the key in p is smaller than or equal to the key in x.
    """
    def __init__(self):
        # Dijkstra’s algorithm requires Priority Queue
        # to store key-value pairs
        # key --> matches the key of the Vertex in the Graph
        # value --> "distance of the key" is used
        #       for deciding the priority and thus, the
        #       position of the key in the Priority Queue
        # WHY DISTANCE OF THE KEY IS USED ?
        # Because we always want to explore the vertex that
        # has the smallest distance
        #
        self.heap_list = [(0, 0)]
        self.current_size = 0

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
        # Starting at the middle and working our way back to the root
        self.current_size = len(alist)
        self.heap_list = [(0, 0)]
        for i in alist:
            self.heap_list.append(i)
        i = len(alist) // 2
        while i > 0:
            # Percolate down until all max values have moved down
            self.perc_down(i)
            i = i - 1

    #
    #   perc_down, min_child and build_heap are used to create a heap from a
    #   given list of elements
    #

    def perc_down(self, i):
        """
        **Ensures that the largest child is always moved down the tree**
        Adjust the binary heap after removal of min node by maintaining
        the heap order property
        Args:
            i(int): index of node to percolate down
        """
        # Check if left child exists for current value of i
        while (i * 2) <= self.current_size:
            # Find the index of minimum valued child
            mc = self.min_child(i)
            # Swap if parent value is greater than
            # minimum child's value
            if self.heap_list[i][0] > self.heap_list[mc][0]:
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
        if i * 2 > self.current_size:
            return -1
        else:
            if i * 2 + 1 > self.current_size:
                return i * 2
            else:
                if self.heap_list[i * 2][0] < self.heap_list[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    #
    #   perc_up, insert are used to create a heap
    #   taking a single item at a time
    #

    def perc_up(self, i):
        """
        **Ensures that the smallest child is always moved up the tree**
        Adjust the binary heap to maintain the heap order property
        """
        # While parent exist
        while i // 2 > 0:
            # If item is less than its parent,
            # then we can swap the item with its parent.
            if self.heap_list[i][0] < self.heap_list[i // 2][0]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
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
        ret_val = self.heap_list[1][1]
        # Move the last node to make it the new root node
        self.heap_list[1] = self.heap_list[self.current_size]
        # Decrement current size by 1
        self.current_size = self.current_size - 1
        # Remove the last item from the heap_list as it is now moved to the root
        self.heap_list.pop()
        # Call perc_down to ensure that the largest child is always moved down the tree
        self.perc_down(1)
        return ret_val

    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def decrease_key(self, vertex, new_dist):
        """
        This method is used when the distance to a vertex
        that is already in the queue is reduced, and thus
        moves that vertex toward the front of the queue.
        Args:
            vertex(Vertex): Vertex to check
            new_dist(int): Updated distance for the Vertex object
        """
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.current_size:
            if self.heap_list[i][1] == vertex:
                done = True
                myKey = i
            else:
                i = i + 1
        if myKey > 0:
            self.heap_list[myKey] = (new_dist, self.heap_list[myKey][1])
            self.perc_up(myKey)

    def __contains__(self, vtx):
        for pair in self.heap_list:
            if pair[1] == vtx:
                return True
        return False