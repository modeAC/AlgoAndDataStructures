def hash(str):
    h = 0
    for ltr in str:
        h = ord(ltr) + 31*h
    return h


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0

    def index(self, str, capacity):
        return hash(str)%capacity

    def __setitem__(self, key, value):
        ind = self.index(key, self.capacity)
        while self.keys[ind] is not None:
            if self.keys[ind] == key and self.values[ind] == value:
                return
            ind = (ind + 1) % self.capacity
        self.keys[ind] = key
        self.values[ind] = value
        self.size += 1
        if self.size / self.capacity > 0.75:
            self.resize()

    def __getitem__(self, key):
        ind = self.index(key, self.capacity)

        while self.keys[ind] is not None:
            if self.keys[ind] == key:
                return self.values[ind]
            ind = (ind + 1) % self.capacity
        return None

    def resize(self):
        new_capacity = 2 * self.capacity
        new_keys = [None] * new_capacity
        new_values = [None] * new_capacity
        for i in range(self.capacity):
            key = self.keys[i]
            value = self.values[i]
            if key:
                ind = self.index(key, new_capacity)
                while new_keys[ind] is not None:
                    ind = (ind + 1) % new_capacity
                new_keys[ind] = key
                new_values[ind] = value
        self.capacity = new_capacity
        self.keys = new_keys
        self.values = new_values

    def __len__(self):
        return self.size


class HashSet:
    def __init__(self):
        self.table = HashTable(100)

    def add(self, key):
        self.table[key] = key

    def __contains__(self, item):
        var = self.table[item]
        return var is not None

    def __len__(self):
        return self.table.size