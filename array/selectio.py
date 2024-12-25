
lst = [2,5,7,8,9,6]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print(lst)