#Single python list to implement three stacks
class MultiStack:
    def __init__(self, list_len):
        assert int(list_len) == list_len and list_len >=3, "please provide valid list len >=3"
        
        stacks_cnt = 3
        
        self.l = ['?'] * list_len
        
        tmp = list_len//3
        
        stack_I= {
            'start': 0,
            'end': tmp - 1,
            'top': '?',
            'rear': '?'
        }
        stack_II = {
            'start': tmp,
            'end': 2*tmp - 1,
            'top': '?',
            'rear': '?'
        }
        
        stack_III = {
            'start': 2*tmp,
            'end': list_len-1,
            'top': '?',
            'rear': '?'
        }
        
        self.stacks = {1: stack_I, 2: stack_II, 3: stack_III}
        
    def is_valid_stack(self, stack_no):
        assert int(stack_no) == stack_no and 1<=stack_no<=3, "please provide valid stack no in (1, 2, 3)"
        
    def is_stack_full(self, stack_no):
        self.is_valid_stack(stack_no)
        
        if self.stacks[stack_no]['rear'] == self.stacks[stack_no]['end']:
            return True
        
        return False
    
    def is_stack_empty(self, stack_no):
        self.is_valid_stack(stack_no)
        
        if self.stacks[stack_no]['top'] == '?':
            self.stacks[stack_no]['rear'] = '?'
            return True
        
        return False       
        
    def append(self, item, stack_no):
        if self.is_stack_full(stack_no):
            print(f"STACK {stack_no} is full")
            return
        
        if self.is_stack_empty(stack_no):
            self.stacks[stack_no]['top'] = self.stacks[stack_no]['rear'] = self.stacks[stack_no]['start']
            self.l[self.stacks[stack_no]['rear']] = item
            return
        
        if self.stacks[stack_no]['rear'] < self.stacks[stack_no]['end']:
            self.stacks[stack_no]['rear'] += 1
            self.l[self.stacks[stack_no]['rear']] = item
    
    def pop(self, stack_no):
        if self.is_stack_empty(stack_no):
            print(f"STACK {stack_no} is empty")
            return 
        
        if self.stacks[stack_no]['top'] <= self.stacks[stack_no]['rear']:
            self.l[self.stacks[stack_no]['top']] = '?'
            self.stacks[stack_no]['top'] += 1
                    
        #All elements removed from stack
        if self.stacks[stack_no]['top'] - 1 == self.stacks[stack_no]['rear']:
            self.stacks[stack_no]['top'] = self.stacks[stack_no]['rear'] = '?'  
        
    
    def display_stack(self, stack_no):
        if self.is_stack_empty(stack_no):
            print(f"STACK {stack_no} is empty")
            return 
        
        top = self.stacks[stack_no]['top']
        rear = self.stacks[stack_no]['rear']        
        
        while top <= rear:
            print(self.l[top], end=" ")
            top += 1
    
    def get_top(self, stack_no):
        if self.is_stack_empty(stack_no):
            print(f"STACK {stack_no} is empty")
            return
        
        return self.l[self.stacks[stack_no]['top']]
    
    def get_rear(self, stack_no):
        if self.is_stack_empty(stack_no):
            print(f"STACK {stack_no} is empty")
            return
        
        return self.l[self.stacks[stack_no]['rear']]
    
    def __repr__(self):
        s1 = "MultiStack Statistics\n"
        
        s2 = f"List - "
        for i, j in enumerate(self.l):
            s2 += f"{i}:{j} "
                
        s3 = f"\nStack I - {self.stacks[1]}\n"
        s4 = f"Stack II - {self.stacks[2]}\n"
        s5 = f"Stack III - {self.stacks[3]}\n"
    
        return s1+s2+s3+s4+s5
            
s = MultiStack(10)
stackI = 1
stackII = 2
stackIII = 3

s.append(10, stackIII)
s.append(11, stackIII)
s.append(22, stackIII)
s.append(33, stackIII)
print(s)
# s.pop(stackII)
# s.pop(stackII)
# s.append(44, stackII)
# print(s)
# # s.append(22, stackI)
# # s.pop(stackI)
# # s.pop(stackI)
# # s.pop(stackI)
# # print(s)
print(s.get_top(stackIII), s.get_rear(stackIII))
