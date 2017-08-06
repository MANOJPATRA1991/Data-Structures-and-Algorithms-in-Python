class HashTable(object):
    """Implements the map abstract data type """

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """ Insert data with key into hash table """
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # replace the data if key already exists
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                # there is collision
                # linear probing needs to be done
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and \
                                self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key

                self.data[next_slot] = data

    def get(self, key):
        """ Get the value for a specified key
        from the Hash table """
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

                if position == start_slot:
                    stop = True
        return data

    # these methods allow access using '[]'

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size
