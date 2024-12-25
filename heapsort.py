def sorted(arr):
    n= len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,i,n)

    for i in range(n-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)
    
def heapify(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    largest = i

    if left<n and arr[left] >arr[largest]:
        largest = left
    if right <n and arr[right] >arr[largest]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,largest,n)
    
arr =  [6,2,7,3,9,1,5,17]
print(arr)
sorted(arr)
print(arr)