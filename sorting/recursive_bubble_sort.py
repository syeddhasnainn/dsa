arr = [13,46,24,52,20,9]
n = len(arr)

def bubble_sort(arr, n):
    if n == 1:
        return

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    n -= 1
    return bubble_sort(arr, n)

bubble_sort(arr, n)

