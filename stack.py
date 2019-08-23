'''
    STACK - linear data structure
    LIFO - last in first out
'''

class Stack():
    def __init__(self):
        self.stack_list = []

    def add_item(self, item):
        self.stack_list.append(item)
        print("Item {} added to stack".format(item))

    def del_item(self):
        if len(self.stack_list):
            print("Item {} removed from stack".format(self.stack_list[-1]))
            self.stack_list.pop()
        else:
            print("Stack is empty, no scope for deletion")

    def __str__(self):
        if len(self.stack_list):
            return "Stack of elements:{}".format(self.stack_list)
        else:
            return "Stack is empty"

st = Stack()
print(st)
st.add_item(10)
st.add_item(110)
st.add_item(1110)
st.add_item(11110)
print(st)
st.del_item()
st.del_item()
print(st)
st.del_item()
st.del_item()
st.del_item()
st.del_item()
