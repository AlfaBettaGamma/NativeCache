class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        index = 0
        val = str(value)
        for i in range(len(val)):
            if int(val[i]) != 0:
                index += int(val[i]) * (i+1)
            elif int(val) == 0:
                index = 0
                return index
            else:
                index += 17 * (i + 1)
        if self.size != 0:
            index = index % self.size
        return index

    def seek_slot(self, value):
        x = self.size - 1
        index = self.hash_fun(value)
        if x == 0:
            if self.slots[index] is None:
                return index
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            else:
                index += self.step
                while index > x:
                    if x == 0:
                        index -= 1
                    index -= x
                if self.slots[index] is None:
                    return index
        return None

    def put(self, value):
        x = self.seek_slot(value)
        if x is not None:
            self.slots[x] = value
            return x
        else:
            return None

    def find(self, value):
        x = self.size - 1
        index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] == value:
                return index
            else:
                index += self.step
                while index > x:
                    index -= x
                if self.slots[index] == value:
                    return index
        return None