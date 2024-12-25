# def reverse(n):
#     if len(n)<=0:
#         return n
#     else:
#         return reverse(n[1:])+n[0]
    
# a = reverse('abcdef')
# print(a)


s = 'abcdef'

for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
    