def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    
    # Merge each side together
    return  merge(left, right, arr.copy())


def merge(left, right, merged):

    i, j = 0, 0
    while i < len(left) and j < len(right):
      
        # Sort each one and place into the result
        if left[i] <= right[j]:
            merged[i+j]=left[i]
            i += 1
        else:
            merged[i + j] = right[j]
            j += 1
            
    for i in range(i, len(left)):
        merged[i + j] = left[i]
        
    for j in range(j, len(right)):
        merged[i + j] = right[j]

    return merged

