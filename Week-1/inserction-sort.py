
def insertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A
A = [int(x) for x in input("Enter numbers: ").split(",")]
print(insertionSort(A))

