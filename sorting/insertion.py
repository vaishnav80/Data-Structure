# def insert(lst):
#     for i in range(1,len(lst)):
#         key = lst[i]
#         j = i-1
#         while j>=0 and lst[j]>key:
#             lst[j+1] = lst[j]
#             j-=1
#         lst[j+1] = key
    
#     return lst

# lst = [6,4,5,8,9,2,1]

# print(insert(lst))

def insert(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and lst[j]>key:
            lst[j+1] = lst[j]
            j-=1

        lst[j+1] = key
    return lst

lst = [6,4,5,8,9,2,1]

print(insert(lst))









def insert(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        while j>=0 and lst[j]>key:
            lst[j+1] =lst[j]
            j-=1
        lst[j+1] = key
    
    return lst

lst = [6,4,5,8,9,2,1]
print(insert(lst))

    