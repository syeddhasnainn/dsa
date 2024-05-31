arr = [2,5,1,3,0]

maxi = float('-inf')
second_max = float('-inf')

for i in range(len(arr)):
    if arr[i] > maxi:
        second_max = maxi
        maxi = arr[i]
    elif arr[i] != maxi and arr[i] > second_max:
        second_max = arr[i]

print(second_max)