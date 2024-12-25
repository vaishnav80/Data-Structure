# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))



def factorial(data):
    if data == 0:
        return 1
    return data * factorial(data-1)

print(factorial(5))