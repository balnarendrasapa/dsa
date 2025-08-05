def getPermutations(nums, result):
    if len(nums) == 1:
        return [nums]
    
    if len(nums) == 2:
        return [[nums[0], nums[1]], [nums[1], nums[0]]]

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = getPermutations(nums, [])
        for p in perms:
            p.append(n)

        result.extend(perms)
        nums.append(n)

    return result

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return getPermutations(nums, [])
