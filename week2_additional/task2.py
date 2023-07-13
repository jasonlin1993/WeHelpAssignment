def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = two_sum([2, 11, 7, 15], 9)
print(result)  # show [O, 2] because nums[O]+nums[2] is 9
