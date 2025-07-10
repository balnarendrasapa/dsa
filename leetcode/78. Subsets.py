def getSubsets(nums, i, subsets, subset):
    if i == len(nums):
        subsets.append(subset[:])
        return

    subset.append(nums[i])
    getSubsets(nums, i + 1, subsets, subset)

    subset.pop()
    getSubsets(nums, i + 1, subsets, subset)



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        getSubsets(nums, 0, subsets, [])

        return subsets
