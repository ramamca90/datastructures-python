def selection_sort(arr):
    
    for i in range(len(arr)):        
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
