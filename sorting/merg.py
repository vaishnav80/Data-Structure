def merge(lst):
    if len(lst)>1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i < len(left)  and j<len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i+=1
            else:
                lst[k] = right[j]
                j+=1
            k+=1
        
        while i<len(left):
            lst[k] = left[i]
            i+=1
            k+=1
        
        while j<len(right):
            lst[k] = right[j]
            k+=1
            j+=1
        
    return lst


lst = [5,15,8,6,1,9,4]       
print(merge(lst))
            