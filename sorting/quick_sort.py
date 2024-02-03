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

#another way using Lomuto & hoares
#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quick_sort(self, arr, low, high):        
        if low >= high:
            return
        
        # pivot_index = self.lomuto_partition(arr, low, high)
        # self.quick_sort(arr, low, pivot_index-1)
        # self.quick_sort(arr, pivot_index+1, high)
        pivot_index = self.hoares_partition(arr, low, high)
        self.quick_sort(arr, low, pivot_index)
        self.quick_sort(arr, pivot_index+1, high)
    
    def lomuto_partition(self, arr, low, high):
        # code here
        i = low - 1
        pivot = arr[high]
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        
        return i+1
        
    def hoares_partition(self, arr, low, high):
        # hoares partition
        i = low - 1
        j = high + 1
        pivot = arr[low]
        
        while True:
            while True:
                i += 1
                if arr[i] >= pivot:
                    break

            while True:
                j -= 1
                if arr[j] <= pivot:
                    break
                
            if i >= j:
                return j
            
            arr[i], arr[j] = arr[j], arr[i]
        
        return j

#driver code
arr = [10, 7, 8, -9, 9, 9, 4, 5, 6, -9, 1, 5, -9]   
Solution().quick_sort(arr, 0, len(arr)-1)
