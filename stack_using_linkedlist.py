class Node:
    def __init__(self, stack_item):
        self.value = stack_item
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, item):
        node = Node(item)
        
        if not self.top:
            self.top = node
            return
        
        node.next = self.top
        self.top = node
        
    
    def pop(self):
        if not self.top:
            print("stack is empty")
            return
        
        print(f"{self.top.value} removed from STACK")
        self.top = self.top.next
        
    def peek(self):
        if not self.top:
            print("stack is empty")
            return
    
        print(f"Top of the stack - {self.top.value}")
    
    def recursive_print(self, node):
        if not node.next:
            return str(node.value)
        
        return f"{self.recursive_print(node.next)} {node.value}"
        
    def __repr__(self):
        if not self.top:
            return "stack is empty"
        
        curr = self.top
        return self.recursive_print(curr)
        
s = Stack()
print(s)
s.push(10)
print(s)
s.push(11)
print(s)
s.push(12)
print(s)
s.push(13)
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
