# def reverse(n,new = 0):
#     if n ==0:
#         return new
#     else:
#         last = n%10
#         new = new *10 + last
#         return reverse(n//10,new)

# print(reverse(359))
    

def reverse(n):
    if len(n)<=0:
        return n
    else:
        print(n[1:],'dfd')
        return reverse(n[1:])+n[0]

print(reverse('hello'))