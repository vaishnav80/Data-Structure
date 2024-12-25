def function1(arr): 
    n = len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,i,n)
    print(arr)
    for i in range(n-1,-1,-1):
        arr[0],arr[i] = arr[i],arr[0]
        print(arr,'bnmk',i)
        heapify(arr,0,i)

def heapify(arr,i,n):
    largest = i
    left = 2*i+1
    right =  2*i+2
    if left<n and arr[left]>arr[largest]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]

        return heapify(arr,largest,n)
    
lst = [5,2,7,8,9,4,3]
function1(lst)
print(lst)