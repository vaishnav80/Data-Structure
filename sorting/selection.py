# def selection(lst):
#     for i in range(len(lst)):
#         mini = i
#         for j in range(i+1,len(lst)):
#             if lst[j]<lst[mini]:
#                 mini= j

#         lst[i],lst[mini] = lst[mini],lst[i]
    
#     return lst

# lst = [2,8,5,6,4,7]
# print(selection(lst))



# def selection(lst): 

#     for i in range(len(lst)):
#         min = i
#         for j in range(i+1,len(lst)):

#             if lst[j] < lst[min]:

#                 min = j

#         lst[i],lst[min] = lst[min],lst[i]
    
#     return lst

# lst = [2,8,5,6,4,7]
# print(selection(lst))





# def selection(lst):
#     for i in range(len(lst)):
#         min = i
#         for j in range(i+1,len(lst)):
#             if lst[j]<lst[min]:
#                 min = j

#         lst[i],lst[min] = lst[min],lst[i]

#     return lst

def selection(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j]<lst[i]:

                lst[i],lst[j] = lst[j],lst[i]

    return lst

lst = [2,8,5,6,4,7]
print(selection(lst))



