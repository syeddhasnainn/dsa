nums = [1,2,3,4]

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            print(True)