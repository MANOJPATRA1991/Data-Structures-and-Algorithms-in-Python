class BinHeap:
    def __init__(self):
        # zero is the first element to make simple interger division
        # to find index to insert node in
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        """
        Adjust the binary heap to maintain the heap order property
        """
        while i // 2 > 0:
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
        self.perc_up(self.current_size)

    def del_min(self):
        """
        Delete min element
        """
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def perc_down(self, i):
        """
        Adjust the binary heap after removal of min node by maintaining
        the heap order property
        Args:
            i: index of node to percolate down
        """
        while(i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = \
                    self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        """
        Get the min child of an element
        Args:
            i: index of parent
        Returns:
            index of child with minimum value
        """
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
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

bh = BinHeap()
bh.build_heap([9, 5, 6, 2, 3])

print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
