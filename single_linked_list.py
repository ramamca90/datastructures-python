class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class singleLinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        else:
            return True

    def add_at_end(self, node):
        if self.is_empty():
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = node

    def add_at_front(self, node):
        if self.is_empty():
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def insert_between_nodes(self, newnode, data1, data2):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.head
            while temp and temp.next:
                if temp.data == data1 and temp.next.data == data2:
                    newnode.next = temp.next
                    temp.next = newnode
                    return
                temp = temp.next

        print(data1 + " and/or " + data2 + " nodes not exists")

    def insert_at(self, node, pos):
        if self.is_empty():
            self.head = node
            print("List is empty , created at 0 position")
            return
        if pos == 0:
            self.add_at_front(node)
            return

        temp = self.head

        while pos > 1 and temp.next:
            temp = temp.next
            pos -= 1

        if temp.next is None:
            print("Looks position {} is out of range, so adding node at end".format(pos))
            temp.next = node
        else:
            node.next = temp.next
            temp.next = node

    def delete_at_end(self):
        if self.is_empty():
            print("List is empty")
        else:

            if self.head.next is None:
                self.head = None
            else:
                prev = temp = self.head
                while temp.next:
                    prev = temp
                    temp = temp.next

                prev.next = None

    def delete_head_node(self):
        if self.is_empty():
            print("List is empty, delete failed")
        else:
            prev =  self.head
            self.head = self.head.next
            prev.next = None

    def delete_at(self, pos):
        if self.is_empty():
            print("List is empty, delete failed")
            return

        if pos == 0:
            self.delete_head_node()
            return

        temp = self.head
        while pos  and temp.next:
            prev = temp
            temp = temp.next
            pos -= 1

        if pos == 0:
            prev.next = temp.next
            temp.next = None
        else:
            print("Please enter valid position , delete failed")

    def display_list(self):
        if self.is_empty():
            return "List empty"
        temp = self.head
        while temp:
            print(temp.data, end ="->")
            temp = temp.next
        print("\n")

'''
list = singleLinkedList()
node = Node("A")

list.add_at_end(node)
node = Node("B")
list.add_at_end(node)
node = Node(100)
list.add_at_front(node)
node = Node(["C", 100, 200,"xx"])
list.add_at_end(node)
node = Node("D")
list.add_at_end(node)
node = Node("E")
list.add_at_end(node)
node = Node("F")
list.add_at_end(node)
node = Node("G")
list.add_at_end(node)
node = Node("H")
list.add_at_end(node)
node = Node(999)
list.insert_between_nodes(node, 100, "A")
node = Node(23)
list.insert_at(node, 5) #node ,pos
#list.delete_at_end()
list.display_list()
#list.delete_head_node()
list.delete_at(1)
list.display_list()
'''
