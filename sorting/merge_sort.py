arr = [1,3,6,2,8,2,5,9]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = int(len(arr) / 2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return(left, right)

a = merge_sort(arr)
print(a)


