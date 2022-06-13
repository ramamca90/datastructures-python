class Tree:
    def __init__(self, data, childs=None):
        self.data = data
        self.childs = childs
        if not childs:
            self.childs = []
            
    def __repr__(self, level=0):
        result = f"{' '*level}{self.data}\n"
        level += 1
        for child in self.childs:
            result += child.__repr__(level)
            
        return result
    
    def add_child(self, child):
        self.childs.append(child)

tree = Tree('root')
c1 = Tree('C1')
c2 = Tree('C2')
c3 = Tree('C3')

tree.add_child(c1)
tree.add_child(c2)
tree.add_child(c3)

c1_1 = Tree('C1_1')
c1_2 = Tree('C1_2')

c1.add_child(c1_1)
c1.add_child(c1_2)

c2_1 = Tree('C2_1')
c2_2 = Tree('C2_2')

c2.add_child(c2_1)
c2.add_child(c2_2)

c2_2_1 = Tree('c2_2_1')
c2_2_2 = Tree('c2_2_2')
c2_2_3 = Tree('c2_2_3')
c2_2_4 = Tree('c2_2_4')

c2_2.add_child(c2_2_1)
c2_2.add_child(c2_2_2)
c2_2.add_child(c2_2_3)
c2_2.add_child(c2_2_4)

print(tree)
