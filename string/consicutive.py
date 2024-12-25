s = 'assnnnnddee'
max = ''
count=1
count2 = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count2+=1
    else:
        if count2>count:
            max = s[i]
            count = count2
            count2 = 1
print(max)

