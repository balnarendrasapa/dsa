from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        q = deque()
        rs = n - k

        for i in range(n):
            q.append(nums[i])
            if rs < n:
                nums[i] = nums[rs]
                rs += 1
            else:
                nums[i] = q.popleft()
            
