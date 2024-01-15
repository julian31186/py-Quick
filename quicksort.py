from random import randrange

def quicksort(l,r,arr):
    if l < r:
        partition_idx = partition(l,r,arr)
        quicksort(l,partition_idx - 1,arr)
        quicksort(partition_idx + 1,r,arr)

def partition(l,r,arr):
    i = l
    pivot = arr[r]

    for j in range(l,r):
        if arr[j] <= pivot:
            arr[j],arr[i] = arr[i],arr[j]
            i += 1

    arr[i],arr[r] = arr[r],arr[i]
    return i