'''
python hash map implementation using list of linked lists, here collisions allowed
 - internal implementation of dictionary
'''
import collections

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_node(self, node):
        self.head = node

    def add_node(self, node):
        temp = self.head
        while temp.next:
            if temp.key == node.key: #key already exists
                temp.value = node.value
                return
            temp =  temp.next

        if temp.key == node.key: #key already exists
            temp.value = node.value
            return

        temp.next = node
    
    def get_node(self, key):
        temp = self.head
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        
        raise KeyError(f'No such key {key} exists')
    
    def delete_node(self, key):        
        #key found at first position of linked list
        if self.head.key == key:
            self.head  = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.key == key:
                temp.next = temp.next.next
                return
            temp = temp.next

        raise KeyError(f'No such key {key} exists')

    def __str__(self):
        temp = self.head

        s = ''

        while temp:
            s += f"  {temp.key}: {temp.value}\n"
            temp = temp.next
        
        return s
        
class HashMap:
    def __init__(self):
        self.arr_size = 100
        self.arr = [None] * self.arr_size

    def get_hash_index(self, key):
        return sum([ord(letter) for letter in str(key)]) % self.arr_size

    def __getitem__(self, key):
        index = self.get_hash_index(key)
        ll = self.arr[index]

        if not ll: #no key exists
            raise KeyError(f'No key {key} exists')
        
        return ll.get_node(key) #get value from linked list

    def __setitem__(self, key, value):
        #check key hashable type or not
        if not isinstance(key, collections.Hashable):
            raise TypeError(f"key {key} unhashable type: {type(key)}")

        index = self.get_hash_index(key)
        n = Node(key, value)

        if not self.arr[index]:
            self.arr[index] = LinkedList()
            self.arr[index].create_node(n)
        else:
            ll = self.arr[index] # getting linked list from self.arr index
            ll.add_node(n)
    
    def __delitem__(self, key):
        index = self.get_hash_index(key)
        ll = self.arr[index]

        if not ll:# no keys exists
            raise KeyError(f'No key {key} exists')

        ll.delete_node(key)
    
    def __repr__(self):
        return "{\n" + "".join([str(ll) for ll in self.arr if ll]) + "}"

    def display_arr(self):
        for i in range(self.arr_size):
            print(i, str(self.arr[i]))

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

    print(d)

    print(d['a']) #KeyError: 'No key a exists'
