arr = [7, 5, 9, 2, 8]

for i in range(len(arr) - 1):
    mini = arr[i] # mini = 7
    for j in range(len(arr)-1):
        
        print('inner loop', j)
        if arr[j] < arr[i]:
            mini = arr[j]

    print('minimum value', mini)
print(arr)
        