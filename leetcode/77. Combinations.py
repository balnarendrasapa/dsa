def getCombs(nums, k):
    if k == 0:
        return 1

    if k == 1:
        return [[i] for i in nums]

    result = []

    for i in range(len(nums)):
        first = nums[i]
        sub = getCombs(nums[i + 1:], k - 1)
        temp = [t + [first] for t in sub]
        result += temp

    return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))

        return getCombs(nums, k)
