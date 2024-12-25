# lst = [10, 23, 45, 70, 11, 15]
# a = 23
# b = 11
# for i in range(len(lst)):
#     if lst[i]==a:
#         i1 = i
#     elif lst[i]==b:
#         i2 = i
    
# print(i1+i2)


# a = 23
# b = 15
# def func(a):
#     lst = [10, 23, 45, 70, 11, 15]
#     lst = sorted(lst)
#     low = 0
#     high = len(lst)-1

#     while low<=high:
#         mid = (low +high)//2
#         print(mid)
#         if lst[mid] == a:
#             print(lst[mid],mid)
#             return lst.index(lst[mid])
            
#         elif a < lst[mid]:
#             high = mid-1
#         else:
#             low = mid+1

# a = func(a)
# b= func(b)
# print(a)
# print(b)
# print(a+b)



# def binary(lst,target,high=0,low = 0):
#     if high==0:
#         high = len(lst)-1

#     if low>=high:
#         return -1
    
#     mid = (low+high)//2
#     if lst[mid]==target:
#         return lst[mid]
    
#     elif target < lst[mid]:
#         high = mid-1
#         return binary(lst,target,high,low)
#     else:
#         low = mid + 1
#         return binary(lst,target,high,low)
    
# lst = [10, 23, 45, 70, 11, 15]
# lst = sorted(lst)
# print(binary(lst,10))

lst = [10, 23, 45, 70, 11, 15]

lst = sorted(lst)
a = 23
low = 0
high = len(lst)-1
flag =0
while low <=high:
    mid = (low+high)//2
    if lst[mid] == a:
        lst[mid] = 0
        flag = 1
    elif a<lst[mid]:
        high = mid-1
    else:
        low = mid+1

if flag == 0:
    print("no data found")
else:

    print(lst)

# def binary(lst,target,low=0,high=0):
#     if 