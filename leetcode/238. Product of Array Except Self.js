/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    leftProduct = 1
    rightProduct = 1
    let res = new Array(nums.length).fill(0)
    for(let i in nums){
        res[i] = leftProduct
        leftProduct *= nums[i]
    }
    for(let i = nums.length - 1; i>=0; i--){
        res[i] *= rightProduct
        rightProduct *= nums[i]
    }
    return res
};
