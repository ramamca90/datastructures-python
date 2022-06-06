class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
    
    def enqueue(self, item):
        node = Node(item)
        if not self.top:
            self.top = self.tail = node
            return
        
        self.tail.next = node
        self.tail = self.tail.next
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        print(f"{self.top.value} removed from Queue")
        self.top = self.top.next
    
    def is_empty(self):
        if not self.top:
            self.tail = None
            return True
        
        return False
    
    def get_top(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        print(f"Top element from queue - {self.top.value}")
        
    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        print(f"Rear element from queue - {self.tail.value}")
    
    def __repr__(self):
        if self.is_empty():
            return "Queue is empty"
        
        result = ''
        curr = self.top
        while curr:
            result += f"{curr.value} "
            curr = curr.next
            
        return result
    
q = Queue()
print(q)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.get_top()
q.get_rear()
q.enqueue(10)
q.enqueue(20)
q.get_top()
q.get_rear()
print(q)
