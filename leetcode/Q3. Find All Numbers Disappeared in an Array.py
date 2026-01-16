class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        r = set(range(1, n + 1))

        return list(r - set(nums))
