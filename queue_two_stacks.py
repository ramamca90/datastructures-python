'''
    Impementing queue with 2 stacks
    Using list data structure
'''


class Queue():
    def __init__(self):
        self.stack1 = [] #Using for enqueue
        self.stack2 = [] #Using for dequeue

    def enqueue(self, item):
        self.stack1.append(item)
        print("Item {} added to stack".format(item))

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty, no scope for deletion")
            return
        
        #if elements present in stack2
        if self.stack2:
            deleted = self.stack2.pop()
            print(f"Item {deleted} removed from queue")
            return
        
        #if there is no elements in stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
        deleted = self.stack2.pop()
        print(f"Item {deleted} removed from queue")


    def __str__(self):
        if not self.stack1 and not self.stack2:
            return "Queue empty"

        if self.stack2 and self.stack1:
            final = self.stack2[::-1]
            final.extend(self.stack1)
            return "{}".format(final)

        if self.stack2:
            return "{}".format(self.stack2[::-1])

        if self.stack1:
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
