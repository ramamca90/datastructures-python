#https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10&ab_channel=codebasics


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def traverse_tree(self, parent, child):
        if child.data < parent.data:
            if parent.left:
                self.traverse_tree(parent.left, child)
            else:
                parent.left = child
        elif child.data > parent.data:
            if parent.right:
                self.traverse_tree(parent.right, child)
            else:
                parent.right = child
        else:
            return
        
    def add_node(self, node):
        if not self.root:
            self.root = node
            return
        
        self.traverse_tree(self.root, node)
        
    def in_order(self, curr):
        if not curr:
            return
        self.in_order(curr.left)
        print(curr.data, end=" ")
        self.in_order(curr.right)
        
    def pre_order(self, curr):
        if not curr:
            return
        print(curr.data, end=" ")
        self.in_order(curr.left)        
        self.in_order(curr.right)
        
    def post_order(self, curr):
        if not curr:
            return

        self.in_order(curr.left)        
        self.in_order(curr.right)
        print(curr.data, end=" ")
        
    def print_tree(self):
        if not self.root:
            print("Tree empty")
            return
        
        self.in_order(self.root)
        print()
        self.pre_order(self.root)
        print()
        self.post_order(self.root)
        
t = BinarySearchTree()
#for item in (15, 12, 27, 7, 14, 20, 88, 23):
for item in (17, 4, 1, 20, 9, 23, 18, 34):
    t.add_node(BSTNode(item))

t.print_tree()
t.root.left.left.data
