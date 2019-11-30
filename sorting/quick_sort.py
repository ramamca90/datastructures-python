'''
        -- QuickSort --
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways.
    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.
The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot, 
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, 
and put all greater elements (greater than x) after x. All this should be done in linear time.
'''
def partition(arr):
    pivot = arr[-1]
    
    l_arr = []
    r_arr = []
    for i in range(len(arr)-1):
        if arr[i] < pivot:
            l_arr.append(arr[i])
        else:
            r_arr.append(arr[i])
            
    pivot_index = len(l_arr) 
    arr = l_arr + [pivot] + r_arr
        
    return pivot_index, arr
    
def quick_sort(arr):
    
    size = len(arr)
    if size < 2:
        return arr
    
    #Get partion index , exact position of pivot
    pi, arr = partition(arr)
    
    left_arr = quick_sort(arr[:pi])
    right_arr = quick_sort(arr[pi+1:])
    
    return left_arr + [arr[pi]] + right_arr
    
#driver code    
quick_sort([10, 7, 8, -9, 9, 9, 4, 5, 6, -9, 1, 5, -9])

#another way
def partition(arr, low, high):
    pivot = arr[high] # pivot 
    
    i = low - 1 # index of smaller element 
    for j in range(low, high):
        if arr[j] < pivot:
             # increment index of smaller element 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1],arr[high] = arr[high],arr[i+1]
    
    pivot_index = i+1      
    return pivot_index
    
def quick_sort(arr, low, high):
    
    if low < high:
    
        #Get partion index , exact position of pivot
        pi = partition(arr, low , high)
    
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    
    return arr

#driver code
arr = [10, 7, 8, -9, 9, 9, 4, 5, 6, -9, 1, 5, -9]   
quick_sort(arr, 0, len(arr)-1)
