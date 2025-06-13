class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        low, high = 0, nums[-1] - nums[0]
        answer = 0

        def mdp(max_diff):

            i = 0
            count = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums [i] <= max_diff:
                    count += 1
                    i += 2
                else:
                    i += 1

            return count >= p 

        while low <= high:
            mid = (low + high) // 2

            if mdp(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
