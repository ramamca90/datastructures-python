def binary_search(start, end, lst, ele):
    if start > end:
        return False
    
    mid = (start+end)//2
    if ele ==  lst[mid]:
        return True
    
    if ele < lst[mid]:
        return binary_search(start, mid-1, lst, ele)
    
    return binary_search(mid+1, end, lst, ele)
binary_search(0, 4, [11, 22, 33, 55, 66], 22)   

'''
def binary_search(lst, ele):
    l = len(lst)
    if lst == [] or (l == 1 and lst[0] != ele):
        return False
    
    # For even no mid will be mid of elements -1
    # 10 20 30 40  mid 20
    # For odd no mid will be mid of elements
    # 10 20 30 40 50 mid 30
    mid = (l//2 + l%2) - 1
    
    if ele ==  lst[mid]:
        return True
    
    if ele < lst[mid]:
        return binary_search(lst[:(l//2)], ele)
    
    return binary_search(lst[(l//2):], ele)        
    
def binary_search(lst, ele):
    start = 0
    end = len(lst) - 1
    
    while True:
        if start > end:
            return False
        mid = (start+end)//2
        
        if ele ==  lst[mid]:
            return True
        
        if ele < lst[mid]:
            end = mid-1
        else:
            start = mid+1
'''
