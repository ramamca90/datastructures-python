
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class CirLinkedList():
    def __init__(self):
        self.head = None

    def is_list_empty(self):
        return True if self.head == None else False

    def add_at_head(self, node):
        if self.is_list_empty():
            self.head = node
            self.head.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        node.next = self.head
        curr.next = node
        self.head = node

    def add_at_end(self, node):
        if self.is_list_empty():
            self.head = node
            self.head.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        node.next = self.head
        curr.next = node
        #self.head = node

    def delete_at_end(self):
        if self.is_list_empty():
            print("List empty")
            return

        curr = self.head
        if curr.next == self.head:
            self.head = None
            return

        while True:
            if curr.next.next == self.head:
                curr.next = self.head
                break
            curr = curr.next

    def delete_at_head(self):
        if self.is_list_empty():
            print("List empty")
            return

        curr = self.head

        if curr.next == self.head:
            self.head = None
            return

        while curr.next != self.head:
            curr = curr.next

        self.head = self.head.next
        curr.next = self.head




    def display_list(self):
        if self.is_list_empty():
            print("\nList empty")
            return

        curr = self.head
        print("")
        while curr.next != self.head:
            print(curr.data , end = '->')
            curr = curr.next

        print(curr.data , end = '->')

#Main logic
clist = CirLinkedList()
# clist.add_at_head(Node(10))
# clist.add_at_head(Node(20))
# clist.add_at_head(Node(30))

clist.add_at_end(Node(10))
clist.add_at_end(Node(20))
clist.add_at_end(Node(30))

clist.display_list()
#clist.delete_at_end()
clist.delete_at_head()
clist.display_list()
