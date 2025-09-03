class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tm = sum(nums) % p

        if tm == 0:
            return 0

        pre = {0: -1}
        curr = 0
        ans = len(nums)

        for i, x in enumerate(nums):
            curr = (curr + x) % p
            w = (curr - tm) % p

            if w in pre:
                ans = min(ans, i - pre[w])
                
            pre[curr] = i

        return -1 if ans == len(nums) else ans



