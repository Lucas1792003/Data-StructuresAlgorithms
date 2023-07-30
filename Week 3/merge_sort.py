def merge_sort(arr):
    if (len(arr)<=1):
        return arr
    
    mid = (len(arr))//2
    left =arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
    
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# arr = [3,2,4,6,2,9,1,0,10,11,15,12]

arr = []
arr = [int(x) for x in input().split(',')]
sorted_arr = merge_sort(arr)
print(sorted_arr)