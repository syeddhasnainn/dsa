arr = [13,46,24,52,20,9]

for i in range(1, len(arr)):
    key = arr[i]
    j = i -1 
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j-= 1
    arr[j+1] = key

print(arr)
