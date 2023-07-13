function maxProduct(nums) {
    // 1. 獲取所有兩兩相乘的結果，但同一數字不乘以自身
    multiplied_nums = []
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            multiplied_nums.push(nums[i] * nums[j])
        }
    }

    // 2. 移除重複的數字
    let unique_nums = []
    for (let num of multiplied_nums) {
        if (!unique_nums.includes(num)) {
            unique_nums.push(num);
        }
    }

    // 3. 找出數字最大的數字
    let max_num = unique_nums[0];
    for (let num of unique_nums) {
        if (num > max_num) {
            max_num = num;
        }
    }
    console.log(max_num)
}
maxProduct([5, 20, 2, 6]) // print 120
maxProduct([10, -20, 0, 3]) // print 30
maxProduct([10, -20, 0, -3]) // print 60
maxProduct([-1, 2]) // print -2
maxProduct([-1, 0, 2]) // print 0 or -0
maxProduct([5, -1, -2, 0]) // print 2
maxProduct([-5, -2]) // print 10