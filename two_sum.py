nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    hash_set = {}

    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in hash_set:
            return [hash_set[comp], i]
        else:
            hash_set[nums[i]] = i
    return []

a = two_sum(nums, target)
print(a)
