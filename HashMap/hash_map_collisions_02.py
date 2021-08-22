'''
python hash map implementation using list of lists here collisions allowed
 - internal implementation of dictionary
'''
import collections
        
class HashMap:
    def __init__(self):
        self.arr_size = 100
        self.arr = [[] for i in range(self.arr_size)] # storing list of lists and dont use -- [[]] * self.arr_size

    def get_hash_index(self, key):
        return sum([ord(letter) for letter in str(key)]) % self.arr_size

    def __setitem__(self, key, value):
        #check key hashable type or not
        if not isinstance(key, collections.Hashable):
            raise TypeError(f"key {key} unhashable type: {type(key)}")

        index = self.get_hash_index(key)
        new_item = (key, value)

        for pos in range(len(self.arr[index])):
            if self.arr[index][pos][0] == key:
                self.arr[index][pos] = new_item
                break
        else:
            self.arr[index].append(new_item)


    def __getitem__(self, key):
        index = self.get_hash_index(key)
        l = self.arr[index]

        for pos in range(len(self.arr[index])):
            if self.arr[index][pos][0] == key:
                return self.arr[index][pos][1]

        raise KeyError(f'No key {key} exists')
    
    def __delitem__(self, key):
        index = self.get_hash_index(key)

        for pos in range(len(self.arr[index])):
            if self.arr[index][pos][0] == key:
                self.arr[index].pop(pos)
                return

        raise KeyError(f'No key {key} exists')
        
    
    def __repr__(self):
        s = "{\n" + "".join([f"  {item[0]}: {item[1]}\n" for l in self.arr for item in l]) + "}"

        return {} if len(s)==3 else s


if __name__ == '__main__':
    d = HashMap()
    
    d['key1d'] = 'value1'
    d['key1dd'] = 'value11'
    d['key1ddd'] = 'value111'
    d['key1dddd'] = 'value1111'
    d['key11111key11111'] = 'value1111value1111'
    d['key111111'] = 'value1111'
    d['key1111111'] = 'value11111'

    print(d)

    del d['key1dddd']
    print(d['key1ddd'])
    print(d)

    print(d['a']) #KeyError: 'No key a exists'
