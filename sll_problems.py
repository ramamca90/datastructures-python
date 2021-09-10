'''
   single linked list problems
'''
from single_linked_list import Node, singleLinkedList

# Function to reverse the linked list using swapping
def reverse(head):
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

# Function to reverse the linked list using recursion
def reverse_rec(node):
    if (node == None):
        return node
    
    if (node.next == None):
        return node
    
    node1 = reverse_rec(node.next)
    node.next.next = node
    node.next = None

    return node1     

def detect_loop(list):
    if list.is_empty():
        print("List is empty")
        return

    if list.head.next is None:
        print("Single element , no loop possible")
        return

    temp = list.head
    s = set()

    while temp:
        if temp in s:
            print("Loop detected")
            return
        s.add(temp)
        temp = temp.next

    print("No loop detected")

def swap_two_nodes(list, node1, node2):
    if list.is_empty():
        print("List is empty")
        return

    if list.head.next is None:
        print("list has single element , nothing to do")
        return

    if node1 == node2:
        print("Swappping nodes same , nothing doing")
        return

    print("Swapping nodes {} {}".format(node1.data, node2.data))

    # Search for node1 (Keep track of prevNode1, currNode1)
    prevNode1 = None
    currNode1 = list.head
    while currNode1 and currNode1 != node1:
        prevNode1 = currNode1
        currNode1 = currNode1.next

    # Search for node2 (Keep track of prevNode2, currNode2)
    prevNode2 = None
    currNode2 = list.head
    while currNode2 and currNode2 != node2:
        prevNode2 = currNode2
        currNode2 = currNode2.next

    # Either node1 or node 2 is not present, nothing to do
    if currNode1 == None or currNode2 == None:
        print("Either node1 or node 2 is not present, nothing to do")
        return

    # If node1 is not head of linked list
    if prevNode1 != None:
        prevNode1.next = currNode2
    else: #Make the currNode2 as head
         list.head = currNode2

    # If node2 is not head of linked list
    if prevNode2 != None:
        prevNode2.next = currNode1
    else: #Make the currNode2 as head
        list.head = currNode1

    list.display_list()

    # Swap next pointers
    temp = currNode1.next
    currNode1.next = currNode2.next
    currNode2.next = temp

if __name__ == '__main__':
    list = singleLinkedList()
    list.head = Node(10)
    list.head.next = Node(20)
    list.head.next.next = Node(30)
    list.head.next.next.next = Node(40)
    list.head.next.next.next.next = Node(50)
    list.head.next.next.next.next.next = Node(60)
    #detect_loop(list)
    list.display_list()
    swap_two_nodes(list, list.head, list.head.next)
    list.display_list()
    list.head = reverse(list.head)
    list.display_list()
    list.head = reverse_rec(list.head)
    list.display_list()
    
