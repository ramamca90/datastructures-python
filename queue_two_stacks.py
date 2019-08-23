'''
    Impementing queue with 2 stacks
    Using list data structure
'''

class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        print("Item {} added to stack".format(item))

    def dequeue(self):
        if self.stack1 == [] and self.stack2 == []:
            print("Queue is empty, no scope for deletion")
            return

        if not len(self.stack2):    # stack 2 empty
            self.stack2 = self.stack1[::-1] # stack 2 =  reverse of stack 1
            self.stack1 = []

        print("Item {} removed from queue".format(self.stack2[-1]))
        self.stack2.pop()

    def __str__(self):
        if self.stack1 == [] and self.stack2 == []:
            return "Queue empty"

        if self.stack2 != [] and self.stack1 != []:
            final = self.stack2[::-1]
            final.extend(self.stack1)
            return "{}".format(final)

        if  self.stack2 != []:
            return "{}".format(self.stack2[::-1])

        if  self.stack1 != []:
            return "{}".format(self.stack1)

qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)

print(qu)
qu.dequeue()
print(qu)

qu.dequeue()
print(qu)
qu.dequeue()
print(qu)
qu.enqueue(33)
qu.enqueue(44)
print(qu)
qu.dequeue()
print(qu)
qu.dequeue()
print(qu)
qu.dequeue()
print(qu)
qu.dequeue()
print(qu)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)

print(qu)
