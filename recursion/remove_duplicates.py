def remove(lst,i=0,new=None):
    if new is None:
        new = []
    
    if i>=len(lst):
        return []
    
    if lst[i] in new:
        return remove(lst,i+1,new)
    else:
        new.append(lst[i])
        return [lst[i]] + remove(lst,i+1,new)
    
print(remove([2,5,2,6]))
