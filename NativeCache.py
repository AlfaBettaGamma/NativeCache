import random


class NativeCache:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, value):  # определяем индекс слота
        index = 0
        val = str(value)
        for i in range(len(val)):
            if ord(val[i]) != 0:
                index += ord(val[i]) * (i+1)
            else:
                index += 17 * (i + 1)
        if self.size != 0:
            index = index % self.size
        return index

    def seek_slot(self, value):  # отыскивает подходящий слот
        index = self.hash_fun(value)
        for i in range(self.size - 1):
            if self.slots[index] is None:
                return index
            else:
                if index + self.step <= self.size - 1:
                    index += self.step
                    if self.slots[index] is None:
                        return index
                elif index + self.step > self.size - 1:
                    index = index + self.step - self.size
                    if self.slots[index] is None:
                        return index
        return None

    def put(self, value, intem):  #
        x = self.seek_slot(value)
        if x is not None:
            self.slots[x] = value
            self.values[x] = intem
            self.hits[x] = 0
        else:
            x = int(self.cleaning_cache()["key"])
            self.slots[x] = value
            self.values[x] = intem
            self.hits[x] = self.cleaning_cache()["av"]

    def find(self, value):
        index = self.hash_fun(value)
        for i in range(self.size - 1):
            if self.slots[index] == value:
                return index
            else:
                if index + self.step <= self.size - 1:
                    index += self.step
                    if self.slots[index] == value:
                        return index
                    elif index + self.step > self.size - 1:
                        index = index + self.step - self.size
                        if self.slots[index] == value:
                            return index
    return None

    def delete_all(self):
        for i in range(self.size):
            self.slots[i] = None
            self.values[i] = None
            self.hits[i] = None

    def get(self, key):
        x = self.find(key)
        if x is not None:
            self.hits[x] += 1
            return self.values[x]
        else:
            return None

    def cleaning_cache(self):
        minimal = self.hits[random.randint(0, self.size - 1)]
        key = None
        av = 0
        for i in range(self.size):
            av += self.hits[i]
            if self.hits[i] <= minimal:
                minimal = self.hits[i]
                key = i
        return {"av": int(av/(self.size - 1)), "key": key}

    def print_all(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(self.slots[i], self.values[i], self.hits[i])
