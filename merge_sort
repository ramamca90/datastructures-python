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
