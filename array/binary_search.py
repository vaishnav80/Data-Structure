# a = int(input('enter'))
# lst = [2,5,7,8,9,6]
# lst = sorted(lst)
# min = 0
# max = len(lst)-1
# while min<=max:
#     mid = (min+max)//2
#     # print(mid)
#     # print(lst[mid],'mid')
#     # if lst[mid] == a:
#     #     print(lst[mid],'answer')
#     # if lst[mid]<a:
#     #     print("step")
#     #     min = mid+1
#     # else:
#     #     print("step2")
#     #     max = mid-1
















# lst = [1,2,3,4,5,6,7,8,9]
# min = 0
# max = len(lst)-1
# a=8
# while min<=max:
#     mid = (min+max)//2
#     if lst[mid] == a:
#         lst[mid] = 0
#     elif a<lst[mid]:
#         max = mid-1
#     else :
#         min = mid+1
    
# print(lst)



# def binary(lst,target,min=0,max=0):
#     if max == 0:
#         max = len(lst)-1
#     mid = (min+max)//2
#     if lst[mid] == target:
#         lst[mid]= 0
#         return lst
#     elif target<lst[mid]:
#         max = mid-1
#     else:
#         min = mid+1
#     return binary(lst,target,min,max)


# lst = [1,2,3,4,5,6,7,8,9]
# target = 8
# print(binary(lst,target))

def num(n,lst=[],i=0):
    if i==len(n)-1:
        return lst
    if n[i]%2 == 0:
        lst.append(n[i])
        return num(n,lst,i+1)
    return num(n,lst,i+1)

print(num([1,2,3,4,5]))