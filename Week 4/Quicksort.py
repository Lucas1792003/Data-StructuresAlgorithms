
def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos)
        quicksort(arr, partition_pos+1, right)

def partition(A, start, end):  
    x = A[end]
    i = start-1
    for j in range(start, end):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[end], A[i+1] = A[i+1], A[end]
    return i+1


arr = [59,37,27,58,433,284,1]
pivotIndex = partition(arr,0,len(arr)-1)
print(pivotIndex)
print(arr, end="\n")


arr = [1,2,3,4,5]
partition(arr,0,len(arr)-1)
print(arr)

arr = [1,2,3,5,6,7,4]
partition(arr, 0, len(arr)-1)
print(arr)

