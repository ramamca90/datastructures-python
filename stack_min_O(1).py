class Stack:
    class Node:
        def __init__(self, value, _min):
            self.value = value
            self.min = _min
            self.next = None
            
    def __init__(self):
        self.top = None
        
    def append(self, item):
        if not self.top:
            self.top = Stack.Node(item, item)
            return
        
        _min = self.top.min if self.top.min <= item else item
        node = Stack.Node(item, _min)
        node.next = self.top
        self.top = node
    
    def pop(self):
        if not self.top:
            print("Stack is empty")
            return
        
        self.top = self.top.next
    
    @property
    def min_value(self):
        if not self.top:
            return "Stack is empty"
        
        return self.top.min
        
    def __repr__(self):
        if not self.top:
            return "Stack is empty"
        
        result = ""
        curr = self.top
        while curr:
            result += f"{curr.value} -> "
            curr = curr.next
            
        return result.rstrip(' -> ')  
            
s = Stack()
print(s, s.min_value)
s.append(10)
print(s, s.min_value)
s.append(2)
print(s, s.min_value)
s.append(3)
print(s, s.min_value)
s.append(-10)
print(s, s.min_value)
s.pop()
print(s, s.min_value)
s.pop()
print(s, s.min_value)
s.pop()
print(s, s.min_value)
s.pop()
print(s, s.min_value)
