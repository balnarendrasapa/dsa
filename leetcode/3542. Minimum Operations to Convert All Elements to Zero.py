class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        result = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()

            if num == 0:
                continue

            if not stack or stack[-1] < num:
                stack.append(num)
                result += 1

        return result
