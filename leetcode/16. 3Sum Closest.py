class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        tracker = float("inf")
        result = 0
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if abs(target - s) < tracker:
                    tracker = abs(target - s)
                    result = s

                if s == target:
                    return s
                elif s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return result
