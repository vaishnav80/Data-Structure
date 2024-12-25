# def prime_finder(prime, i=None):
#     if i is None:
#         if prime <= 1:
#             return False
#         i = int(prime//2) + 1
#         print(i)
#     if i < 2:
#         return True
#     if prime % i == 0:
#         return False
#     return prime_finder(prime, i - 1)

# prime =7 
# print(prime_finder(prime))


def string(s):
    if len(s)<=1:
        return s
    print(s[1:])
    return string(s[1:])+s[0]

print(string('hello world'))


def remove(s,c,lst = ''):
    if len(s)==0:
        return lst
  
    return remove(s[1:],c,s[0]+lst)

print(remove('abcd','d'))