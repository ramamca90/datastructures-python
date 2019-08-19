

class Node():
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def display_list(self):
        if self.is_list_empty():
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end = "--")
                temp = temp.next
            print('\n')

    def add_at_head(self, node):
        if self.is_list_empty():
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node


    def add_at_end(self, node):
        if self.is_list_empty():
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next  = node
        node.prev = temp

    def add_at_pos(self, node, pos):
        if pos < 0:
            print("Enter valid position ")
            return

        if pos == 0:
            self.add_at_head(node)
            return

        temp = self.head
        prevNode = None

        while pos and temp:
            prevNode = temp
            temp = temp.next
            pos -= 1

        if pos > 0:
            print("Enter valid position, position should <= list elements ")
            return

        if pos == 0 and prevNode.next == None:
            prevNode.next  = node
            node.prev = prevNode
            return

        # node.next = temp
        # temp.prev.next = node
        # node.prev = temp.prev
        # temp.prev = node

        node.next = prevNode.next
        node.prev = prevNode
        prevNode.next.prev = node
        prevNode.next = node


##Main logic
list = DoubleLinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.add_at_head(n1)

list.add_at_head(n2)
list.add_at_head(n3)

list.display_list()
list.add_at_pos(Node(40), 4)
list.display_list()
