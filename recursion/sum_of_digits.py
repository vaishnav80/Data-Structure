# def sum(n):
#     if n==0:
#         return 0
#     print(n%10)
#     print(n//10,'hh')
#     return (n%10) + sum(n//10)

# print(sum(123))


def sum(n,a=0):
    if n==0:
        return a
    return sum(n//10,(n%10)+a)

print(sum(123))









