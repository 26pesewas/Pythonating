class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        # define hash number
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        #collision handling
        found = False
        for index,element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
                self.arr[h][index] = (key,value) #update existing key
                found = True
                break

        if not found:
            self.arr[h].append((key, value)) # add a new key-value pair

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None #if key isn't found

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                break


t = HashTable()
# print(t.get_hash('march 24'))
t['march 24'] = "My birthday"
t["february 11"] = "Kelvin's birthday"
print(t['march 24'])
print(t['february 11'])

# del t['march 24']
print(t.arr)

