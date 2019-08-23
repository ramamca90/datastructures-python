'''
    QUEUE - linear data structure
    FIFO - First in first out
'''

class Queue():
    def __init__(self):
        self.items = []

    def push_item(self, item):
        self.items.append(item)
        print("Item {} added to stack".format(item))

    def pop_item(self):
        if len(self.items):
            print("Item {} removed from stack".format(self.items[0]))
            self.items.pop(0)
        else:
            print("Queue is empty, no scope for deletion")

    def __str__(self):
        if len(self.items):
            return "Queue of elements:{}".format(self.items)
        else:
            return "Queue is empty"

qu = Queue()
print(qu)
qu.push_item(10)
qu.push_item(20)
qu.push_item(30)
qu.push_item(40)
print(qu)
qu.pop_item()
qu.pop_item()
qu.pop_item()
print(qu)
