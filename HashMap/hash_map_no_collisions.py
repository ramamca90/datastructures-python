#https://www.youtube.com/watch?v=54iv1si4YCM&t=150s&ab_channel=codebasics
'''
python hash map implementation, here no collisions happens
 - internal implementation of dictionary
'''

class HashMap:
    def __init__(self):
        self.arr = [None]*100

    def get_hash_index(self, key):
        return sum([ord(letter) for letter in str(key)]) % 100

    def __getitem__(self, key):
        index = self.get_hash_index(key)
        return self.arr[index]

    def __setitem__(self, key, value):
        index = self.get_hash_index(key)
        self.arr[index] = value
    
    def __delitem__(self, key):
        index = self.get_hash_index(key)
        self.arr[index] = None

if __name__ == '__main__':
    d = HashMap()
    d['abc'] = 1111
    d['xyz'] = 2222
    d['Mayur'] = 3333
    d['Ram'] = 4444

    print(d.arr)
    print(d['abc'])
    del d['abc']
    print(d.arr)
