import gc

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

    def del_at_head(self):
        if self.is_list_empty():
            print("List is empty, nothing to delete")
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_at_end(self):
        if self.is_list_empty():
            print("List is empty, nothing to delete")
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.prev.next = None

    def del_node(self, dele):
        # if self.is_list_empty():
        #     print("List is empty, nothing to delete")
        #     return
        #
        # if self.head == node:
        #     self.del_at_head()
        #     return
        #
        # temp = self.head
        # while temp.next:
        #     if temp.next == node:
        #         if temp.next.next == None: #last node to be deleted
        #             temp.next = None
        #         else:
        #             temp.next = temp.next.next
        #             temp.next.prev  = temp
        #         return
        #     temp = temp.next
        #
        # print("No such node exists, deletion not possible")

        # Base Case
        if self.head is None or dele is None:
            return

        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is NOT
        # the last node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # Change prev only if node to be deleted is NOT
        # the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        # Finally, free the memory occupied by dele
        # Call python garbage collector
        #gc.collect()

#
# ##Main logic
# list = DoubleLinkedList()
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
#
# list.add_at_head(n1)
#
# list.add_at_head(n2)
# list.add_at_head(n3)
#
# list.display_list()
# # list.add_at_pos(Node(40), 4)
# # list.del_at_head()
# list.del_node(n1)
# list.display_list()
