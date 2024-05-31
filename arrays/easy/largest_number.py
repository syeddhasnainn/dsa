arr = [2,5,1,3,0]

maxi = 0

for i in range(len(arr)):
    if arr[i] > maxi:
        maxi = arr[i]

print(maxi)