'''
Merge Sort
Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, 
calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. 
The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted 
and merges the two sorted sub-arrays into one
'''

# Python program for implementation of MergeSort 

def merge_lists(L, R, arr):
        i = j = k = 0          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
            
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        merge_lists(L, R, arr)

  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
  


def merge_lists(l_arr, r_arr):
    final_arr = []

    l_size = len(l_arr)
    r_size = len(r_arr)
    
    i, j = 0, 0
    
    ##check leaft and right array elements map into final array in ascending order
    while i < l_size and j < r_size:
        if l_arr[i] <= r_arr[j]:
            final_arr.append(l_arr[i])
            i += 1
        else:
            final_arr.append(r_arr[j])
            j += 1
            
    ##copy remaining elements of left array into final array, if there are any
    if i < l_size:
        final_arr.extend(l_arr[i:])
        
    ##copy remaining elements of right array into final array, if there are any
    if j < r_size:
        final_arr.extend(r_arr[j:])
              
    return final_arr      
    
def merge_sort(arr):
    
    size = len(arr)
    if size in (0, 1):
        return arr
    
    mid = (size//2) + (size%2)
    
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    return merge_lists(left_arr, right_arr)
    
#driver code
merge_sort([22222, 1, -1, -4, -99, 100, -999, -4])
