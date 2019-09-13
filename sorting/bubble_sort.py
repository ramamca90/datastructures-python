def bubble_sort(arr):
    
    for i in range(len(arr)):
        # Last i elements are already in place 
        for j in range(len(arr)-i-1):
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort([64, 25, 12, 22, 11, -1])
