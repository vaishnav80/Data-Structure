
lst = [2,5,7,8,9,6]
for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j] > lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
            
print(lst)