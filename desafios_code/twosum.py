
nums = [7, 2, 3, 1, 5]
def twoSum(nums, target):
    for i in range(len(nums)):
        #print(i)
        for j in range(i+1, len(nums)):
            #print("j",j)
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(twoSum(nums, 10))