/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    nums.sort((a, b) => {
        return a-b
    })
    if(nums.length === 0){
        return 0
    }
    let order = new Array(nums.length).fill(0)
    max = 0
    for(let i = 1; i < nums.length; i++){
        if(nums[i] === nums[i-1] + 1){
            order[i] = order[i-1]
            order[i]++
            if(max < order[i]){
                max = order[i]
            }
        }
        if(nums[i] === nums[i-1]){
            order[i] = order[i-1]
        }
    }
    return max + 1
};
