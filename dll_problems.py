from double_linked_list import DoubleLinkedList, Node

def check_prior_node(list):
    '''
    check if the node prior to the middle node is greater
    than its next
    '''

    if list.head == None or list.head.next == None or list.head.next.next == None:
        print("Min 3 nodes should present")
        return 1

    temp = list.head
    cnt = 1
    while temp:
        cnt += 1
        temp = temp.next

    temp = list.head
    mid = cnt // 2 if cnt % 2 != 0 else cnt // 2 - 1
    while mid:
        temp = temp.next
        mid -= 1

    if temp.prev.data > temp.next.data:
        print("Condition exists")
    else:
        print("Condition not exists")

def reverse_list(dlist):
    if dlist.is_list_empty():
        print("List empty")
        return

    currNode = dlist.head
    temp = None
    while currNode:
        temp = currNode.prev
        currNode.prev  = currNode.next
        currNode.next = temp
        currNode = currNode.prev

    if temp:
        dlist.head = temp.prev

def remove_duplicates(dlist):
    if dlist.is_list_empty():
        print("List empty")
        return

    cnt_dict = {}

    curr_node = dlist.head
    while curr_node:
        if curr_node.data in cnt_dict:
            if curr_node.next == None:
                curr_node.prev.next = None
                curr_node.prev = None
            else:
                curr_node.next.prev = curr_node.prev
                curr_node.prev.next = curr_node.next
        else:
            cnt_dict[curr_node.data] = 1

        curr_node = curr_node.next

    print(cnt_dict)

def palindrome_check(dlist):
    if dlist.is_list_empty():
        print("List empty")
        return

    start = end = dlist.head
    while end.next:
        end = end.next

    while True:
        print("xx")
        if ( start == end or start.next == end ) and ( start.data == end.data ):
            print("Its palindrome")
            return

        if start.data != end.data or end.next == start:
            print("Its not a palindrome")
            return

        start = start.next
        end = end.prev

if __name__ == '__main__':
    dlist = DoubleLinkedList()
    # n1 = Node(10)
    # n2 = Node(20)
    # n3 = Node(20)
    # n4 = Node(400)
    # n5 = Node(10)

    n1 = Node('l')
    n2 = Node('e')
    n3 = Node('v')
    n6 = Node('v')
    n4 = Node('e')
    n5 = Node('l')

    dlist.add_at_head(n1)
    dlist.add_at_head(n2)
    dlist.add_at_head(n3)
    dlist.add_at_head(n6)
    dlist.add_at_head(n4)
    dlist.add_at_head(n5)

    #check_prior_node(dlist)
    dlist.display_list()
    #reverse_list(dlist)
    #remove_duplicates(dlist)
    palindrome_check(dlist)
    dlist.display_list()
