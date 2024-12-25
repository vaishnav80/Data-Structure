def sort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,i,n)
    
    for i in range(n-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)

def heapify(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left<n and arr[left]>arr[largest]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,largest,n)

lst = [6,10,8,2,4,3,100]
sort(lst)
print(lst)
        