class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                left = j + 1
                right = n - 1

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]

                    if s == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return list(ans)
