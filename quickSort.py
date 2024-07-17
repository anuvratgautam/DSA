def quickSort(a, left, right):
    if left < right:
        partition_pos = partition(a, left, right)
        quickSort(a, left, partition_pos - 1)
        quickSort(a, partition_pos + 1, right)
    return a

def partition(a, left, right):
    pivot = a[right]
    i = left - 1
    
    for j in range(left, right):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    
    a[i + 1], a[right] = a[right], a[i + 1]
    return i + 1

a = [2, 8, 5, 3, 9, 4, 1]
print(quickSort(a, 0, len(a) - 1))
