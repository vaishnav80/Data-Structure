def odd(n,i=0):
    if i >= len(n):
        return 0
    if n[i]%2!=0:
        return n[i] + odd(n,i+1)
    else:
        return odd(n,i+1)
    

print(odd([2,5,9]))