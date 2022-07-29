# merge sort

def merge_list(_list:list) -> list:
    # devide a list to several list with one value
    
    for x in _list:
      if int(x) != x:
        raise ValueError("input must be int")
    
    if len(_list) == 1:
        return _list
    
    else:
        mid:int = len(_list)//2
        left =  _list[:mid]
        right = _list[mid:]
        
    left:list =  merge_list(left)
    right:list = merge_list(right)
    
    return combine(left, right)


def combine(left:list, right:list) -> list:
    # combine lists and sort
    
    result = []         #list
    len1 = len(left)    #int
    len2 = len(right)   #int
    i = j = 0           #int
    
    while i<len1 and j<len2:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result += left[i:]
    result += right[j:]
    
    return result 
   
