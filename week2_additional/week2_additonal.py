# Addition task 1
print("=== Additional Task 1 ===")


def max_product(nums):
    # 1. 獲取所有兩兩相乘的結果，但同一數字不乘以自身
    multiplied_nums = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            multiplied_nums.append(nums[i]*nums[j])

    # 2. 移除重複的數字
    unique_nums = []
    for num in multiplied_nums:
        if num not in unique_nums:
            unique_nums.append(num)

    # 3. 找到數字最大的數字
    max_num = unique_nums[0]
    for num in unique_nums:
        if num > max_num:
            max_num = num
    return print(max_num)


max_product([5, 20, 2, 6])  # print 120
max_product([10, -20, 0, 3])  # print 30
max_product([10, -20, 0, -3])  # print 60
max_product([-1, 2])  # print -2
max_product([-1, 0, 2])  # print 0
max_product([5, -1, -2, 0])  # print 2
max_product([-5, -2])  # print 10

'''
------------------------------------------------------------------------------------------
'''

# Addition task 2
print("=== Addition Task 2 ===")


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = two_sum([2, 11, 7, 15], 9)
print(result)  # show [O, 2] because nums[O]+nums[2] is 9
