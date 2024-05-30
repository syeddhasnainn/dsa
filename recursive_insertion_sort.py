arr = [13,46,24,52,20,9]
n = len(arr)
i = 1
def insertion_sort(arr, n, i):
    if n == i:
        return
    
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j-= 1
    arr[j+1] = key
    i += 1
    print(arr)
    return insertion_sort(arr, n, i)

insertion_sort(arr, n, i)
    