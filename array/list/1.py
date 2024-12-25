
# lst.append(5)
# lst.insert(3,9)
# lst.remove(4)
# lst[2] = 5
lst = [2,4,6,9,9]
# for i in range(int(len(lst)/2)):
#     lst[i],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[i]
max1,max2= 0,0
for i in lst:
    if i>max1:
        max2 = max1
        max1 = i
    elif i > max2 and i < max1:
        max2 = i

print(max1*max2)