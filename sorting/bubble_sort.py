def bubble_sort(arr):
    swapped = false
    for i in range(len(arr)):
        
        # Last i elements are already in place 
        for j in range(len(arr)-i-1):
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
         #if no two elements were swapped by inner loop, then break
         if not swapped:
            break
    return arr

bubble_sort([64, 25, 12, 22, 11, -1])

#recursive solution
# def bubble_sort(arr):
#     size = len(arr)
#     if size == 1:
#         return arr
#     for i in range(size-1):
#         if arr[i] > arr[i+1]:
#             arr[i] , arr[i+1] = arr[i+1], arr[i]
    
#     return bubble_sort(arr[:size-1]) + arr[-1:]
    

