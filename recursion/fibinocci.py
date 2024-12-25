# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
    
#     return fib(n-1)+fib(n-2)

# print(fib())

def no(n,lst=[]):
    if n==0 :
        print(lst)
        return
    print(n)
    lst.append(n)
    no(n-1,lst)
    print('nothing',n)
    lst.pop()

def rec(n,stack=[]):
    if n==0:
        print('call stack',stack)
        return
    stack.append(n)
    print('yes')
    rec(n-1,stack)
    print('noooo')
    no(n)

rec(3)