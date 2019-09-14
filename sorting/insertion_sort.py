def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
                
    return arr
 
 
#driver code
insertion_r_sort([12, 11, -1, 13, 5, 6,-5])
        
#recursive

def insertion_r_sort(arr, key_index):
    
    if key_index == len(arr):
        return arr
    
    key = arr[key_index]
    j = key_index-1
        
    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position
    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
                
    return insertion_r_sort(arr, key_index+1)
    
    #driver code
    insertion_r_sort([12, 11, -1, 13, 5, 6,-5], 1)
