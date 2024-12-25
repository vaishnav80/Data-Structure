lst = [1,2,3,4,1,2,3,4,5,6,7,12,13,14,15,16,17]
new = []
count = 1
for i in range(len(lst)-1):
    
    if lst[i]+1==lst[i+1] :
        count +=1 
    else:
        new.append(count)
        count = 1

print(max(new))
