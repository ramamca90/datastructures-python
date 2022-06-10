#Implement STACK using 2 QUEUES 
#https://leetcode.com/problems/implement-stack-using-queues/submissions/

class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.empty():
            return "Stack is empty"
        
        l = len(self.q1)-1
        for i in range(0, l):
            self.q2.append(self.q1.pop(0))
            
        result = self.q1.pop()
        
        self.q1, self.q2 = self.q2, self.q1
        
        return result
        

    def top(self) -> int:
        if self.empty():
            return "Stack is empty" 
        
        if self.q1:
            return self.q1[-1]
        
        if self.q2:
            return self.q2[-1]
        

    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        
        return False
