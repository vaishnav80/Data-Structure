def sort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,i,n)
        
    for i in range(n-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,0,i)
    return arr

def heapify(arr,i,n):
    left = 2*i+1
    right = 2*i+2
    larger = i
    if left < n and arr[left] > arr[larger]:
        larger = left
    if right <n and arr [right] > arr[larger]:
        larger = right
    if larger!= i:
        arr[larger],arr[i] = arr[i],arr[larger]
        heapify(arr,larger,n)
    
arr = [2,5,8,6,9,4]
sort(arr)
print(arr)