# def quick(lst):
#     if len(lst)<=1:
#         return lst
    
#     pivot = lst[0]
#     left = [x for x in lst if x < pivot]
#     right = [x for x in lst if x > pivot]
#     middle = [x for x in lst if x == pivot]

#     return quick(left) + middle + quick(right)

# print(quick([5,3,8,16,2,1]))







def quick(lst):
    if len(lst)<=1:
        return lst
    pivot = lst[0]
    left = [x for x in lst if x < pivot]
    right = [x for x in lst if x > pivot]
    middle = [x for x in lst if x == pivot]

    return quick(left) + middle + quick(right)

print(quick([5,3,8,16,2,1]))