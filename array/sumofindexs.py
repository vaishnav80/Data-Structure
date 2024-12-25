def f(n):
    # print(n,'stack')
    if n<=1:
        return
    f(n-1)
    print(n,'dfsdhfbs')
    f(n-1)
    print(n,"qwerty")
    print()

print(f(5))