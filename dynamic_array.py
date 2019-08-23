import ctypes
import sys

class DynamicArray(object):
    def __init__(self):
        self.capacity = 1
        self.count = 0
        self.array = self.make_an_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitem__(self, pos):
        if not 0 <= pos < self.count:
            raise IndexError('Its out of bound')

        return self.array[pos]

    def make_an_array(self, required_size):
        return (required_size * ctypes.py_object)()

    def append(self, ele):
        if self.count == self.capacity:
            self._resize_(2*self.capacity) #Double the size

        self.array[self.count] = ele
        self.count += 1

    def _resize_(self, new_capacity):
        self.capacity  = new_capacity
        new_arr = self.make_an_array(self.capacity)

        for i in range(self.count):
            new_arr[i] = self.array[i]

        self.array = new_arr

    def __str__(self):
        if self.count == 0:
            return "Array is empty"

        elements = 'Array: '
        for i in range(self.count):
            elements += "{} ".format(self.array[i])
            #elements += str(self.array[i]) + " "

        return elements

arr = DynamicArray()
print(sys.getsizeof(arr.array))
arr.append(10)
len(arr)
arr.append(20)
arr.append(30)
arr.append(40)
print(sys.getsizeof(arr.array))
#len(arr)
print(arr)
