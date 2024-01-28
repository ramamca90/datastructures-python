'''
        -- Selection Sort --
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray 
is picked and moved to the sorted subarray.
'''

def selection_sort(arr):
    
    for i in range(len(arr)-1):        
        # Find the minimum element in remaining  
        # unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        # Swap the found minimum element with  
        # the first element 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

selection_sort([64, 25, 12, 22, 11, -1])
