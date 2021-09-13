#https://www.youtube.com/watch?v=lFq5mYUWEBk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=10&ab_channel=codebasics


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def tree_height(self, node):
        if not node:
            return 0
        
        lheight = self.tree_height(node.left)
        rheight = self.tree_height(node.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight + 1
        
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
        
    def print_tree(self, node):
        if not node:
            print("Tree empty")
            return
        print("In order", end=" ")
        self.in_order(node)
        print("\nPre order", end=" ")
        self.pre_order(node)
        print("\nPost order", end=" ")
        self.post_order(node)
        print()
        
    def search(self, value, curr_node):
        
        if not curr_node:
            return f"Element {value} NOT found"
            
        if value == curr_node.data:
            return f"Element {value} found"
        
        if value < curr_node.data:
            return self.search(value, curr_node.left)
        else:
            return self.search(value, curr_node.right)
        
    def left_view_tree(self, node, level, max_level):
        if not node:
            return None
        
        if max_level[0]<level:
            print(node.data, end=" ")
            max_level[0] = level
            
        self.left_view_tree(node.left, level+1, max_level)
        self.left_view_tree(node.right, level+1, max_level)
        
    def right_view_tree(self, node, level, max_level):
        if not node:
            return None
        
        if max_level[0]<level:
            print(node.data, end=" ")
            max_level[0] = level
            
        self.right_view_tree(node.right, level+1, max_level)
        self.right_view_tree(node.left, level+1, max_level)
        
    def find_min(self, curr_node):            
        if not curr_node:
                return "Tree is empty"
            
        if curr_node and not curr_node.left:
            return curr_node.data
        
        return self.find_min(curr_node.left)
    
    
    def find_max(self, curr_node):
        if not curr_node:
                return "Tree is empty"
            
        if curr_node and not curr_node.right:
            return curr_node.data
        
        return self.find_max(curr_node.right)
        
    def calculate_sum(self, curr_node):
        
        if not curr_node:
            return 0
            
        left_sum = self.calculate_sum(curr_node.left)
        curr_node_value = curr_node.data
        right_sum = self.calculate_sum(curr_node.right)
        
        return left_sum + curr_node_value + right_sum
        
    def delete(self, value, node):
        if not node:
            print(f"Element {value} not found")
            return

        if value < node.data:
            node.left  = self.delete(value, node.left)

        elif value > node.data:
            node.right = self.delete(value, node.right)
        else:
            #case1 - both left and right are empty
            if not node.left and not node.right:
                return None

            #case2 - only left is empty
            if not node.left:
                return node.right
            #case2 - only right is empty
            if not node.right:
                return node.left

            #case3 - left & right are not empty
            min_val = self.find_min(node.right)
            node.data = min_val
            node.right = self.delete(min_val, node.right)
            
            #or
            #max_val = self.find_max(node.left)
            #node.data = max_val
            #node.left = self.delete(min_val, node.left) 
            
        
        return node
        

if __name__ == '__main__':
    t = BinarySearchTree()
    for item in (17, 4, 1, 20, 9, 23, 18, 34):
    #for item in (17,):
        t.add_node(BSTNode(item))

    t.print_tree(t.root)
    #print(t.search(222, t.root))
    #print(t.search(23, t.root))

    #print(t.find_min(t.root))
    #print(t.find_max(t.root))
    #print(t.calculate_sum(t.root))
    #t.root = t.delete(18, t.root)
    #t.print_tree(t.root)
    print(t.tree_height(t.root))
    #print left view tree
    max_level = [0]
    level = 1
    t.left_view_tree(t.root, level, max_level)
    print()
    #print right view tree
    #print left view tree
    max_level = [0]
    level = 1
    t.right_view_tree(t.root, level, max_level)
