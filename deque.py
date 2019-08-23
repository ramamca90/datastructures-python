'''
    DEQUE - double ended queue
    insertion & deletion at both the ends
'''

class Deque():
    def __init__(self):
        self.items = []

    def insert_at_front(self, item):
        self.items.insert(0, item)
        print("Deque - item {} inserted at front ".format(item))

    def insert_at_end(self, item):
        self.items.append(item)
        print("Deque - item {} inserted at end ".format(item))

    def is_empty(self):
        #return self.items == []
        return not len(self.items)

    def delete_at_front(self):
        if self.is_empty():
            print("Deque - its empty, no scope for deletion")
        else:
            print("Deque - item {} deleted from front ".format(self.items[0]))
            self.items = self.items[1:]


    def delete_at_end(self):
        if self.is_empty():
            print("Deque - its empty, no scope for deletion")
        else:
            print("Deque - item {} deleted from front ".format(self.items[-1]))
            self.items.pop()

    def get_front(self):
        if self.is_empty():
            print("Deque - its empty")
        else:
            print("Deque - item {} at front ".format(self.items[0]))

    def get_rear(self):
        if self.is_empty():
            print("Deque - its empty")
        else:
            print("Deque - item {} at end ".format(self.items[-1]))

    def __str__(self):
        if self.is_empty():
            return "Deque - its empty"
        else:
            return "Deque - {}".format(self.items)


deque = Deque()
print(deque)
deque.insert_at_front(100)
deque.insert_at_front(200)
print(deque)
deque.insert_at_end(300)
deque.insert_at_end(400)
print(deque)
deque.delete_at_front()
print(deque)
deque.delete_at_end()
print(deque)
