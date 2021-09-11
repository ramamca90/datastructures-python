#https://www.youtube.com/watch?v=4r_XR9fUPhQ&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

class Tree:
    def add_child(self, parent, child):
        child.parent = parent
        parent.children.append(child)
    
    def display(self, node, space=0):
        indent = ''
        if space>0:
            indent = "   " * (space-1) + "|__"
        print(f"{indent}{node.data}")
        
        for child in node.children:
            self.display(child, space+1)
        

t = Tree()
r = Node('root')
c1 = Node('c1')
c2 = Node('c2')
c3 = Node('c3')

t.add_child(r, c1)
t.add_child(r, c2)
t.add_child(r, c3)

t.add_child(c1, Node('c11'))
t.add_child(c1, Node('c12'))
t.add_child(c1, Node('c13'))

t.add_child(c2, Node('c21'))
t.add_child(c2, Node('c22'))
t.add_child(c2, Node('c23'))

t.display(c2)

'''
c2
|__c21
|__c22
|__c23
'''

t.display(r)
'''

root
|__c1
   |__c11
   |__c12
   |__c13
|__c2
   |__c21
   |__c22
   |__c23
|__c3

'''
  
