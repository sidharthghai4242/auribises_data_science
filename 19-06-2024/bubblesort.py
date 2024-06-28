nums = [20, 100, 10, 25, 45, 30]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            temp = nums[j + 1]
            nums[j + 1] = nums[j]
            nums[j] = temp

print(nums)
