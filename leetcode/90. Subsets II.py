
def getSubsets(nums, i, subsets, subset):
    subsets.append(subset[:])

    for j in range(i, len(nums)):
        if j > i and nums[j] == nums[j - 1]:
            continue

        subset.append(nums[j])
        getSubsets(nums, j + 1, subsets, subset)
        subset.pop()



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        getSubsets(nums, 0, subsets, [])

        return subsets
