class HashTable(object):
    """
    Implements the map abstract data type
    using Open Addressing
    """

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """
        Insert data with key into hash table
        Args:
            key: The slot in which to insert
            data: Data to insert
        """
        hash_value = self.hash_function(key, len(self.slots))

        # If slot is empty, insert data in the slot
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # Replace the data if key already exists
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                # There is collision
                # Linear probing needs to be done
                next_slot = self.rehash(hash_value, len(self.slots))
                # Continue to search the next slot until we find
                # an empty slot or a slot with the same key
                while self.slots[next_slot] is not None and \
                        self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key

                self.data[next_slot] = data

    def get(self, key):
        """
        Get the value for a specified key from the Hash table
        Args:
            key: The position from which data needs to be retrieved
        """
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        # Keeps track of the position
        position = start_slot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                # If cycled through the slots and reached at the
                # same position, stop the loop and return None as data is not found
                if position == start_slot:
                    stop = True
        return data

    def remove(self, key):
        """
        Remove the value for a specified key from the Hash table
        Args:
            key: The position from which data needs to be deleted
        """
        start_slot = self.hash_function(key, len(self.slots))
        stop = False
        found = False
        # Keeps track of the position
        position = start_slot
        print(position)
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                del self.slots[position]
                data = self.data[position]
                del self.data[position]
                return
            else:
                position = self.rehash(position, len(self.slots))
                # If cycled through the slots and reached at the
                # same position, stop the loop and return None as data is not found
                if position == start_slot:
                    stop = True

    # these methods allow access using '[]'

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        self.remove(key)

    def __len__(self):
        count = 0
        for i in range(0, len(self.slots)):
            if self.slots[i] is not None:
                count += 1
        return count

    def __contains__(self, key):
        return self.get(key)

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        # Skip slots by one
        return (old_hash + 1) % size


h = HashTable()
h[10] = 'A'
h[11] = 'B'
h[12] = 'C'
h[1] = 'D'
h[14] = 'C'
h[15] = 'C'
h[16] = 'C'
h[17] = 'C'
h[18] = 'C'
h[19] = 'C'
h[20] = 'C'
print(h[10])
print(len(h))
