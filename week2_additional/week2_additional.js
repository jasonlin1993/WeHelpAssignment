// Additional task 1 
console.log("=== Additional Task 1 ===")
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

/*
------------------------------------------------------------------------------------------------------------
*/

// Additional Task 2
console.log("=== Additional Task 2 ===")

function twoSum(nums, target){
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j]
            }
        }
    }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [O, 2] because nums[O]+nums[2] is 9