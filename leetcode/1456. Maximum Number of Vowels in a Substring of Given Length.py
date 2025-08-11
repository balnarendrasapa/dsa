class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        window_start = 0
        window_end = k - 1

        max_v = float("-inf")
        vs = set(['a', 'e', 'i', 'o', 'u'])

        count = 0
        for char in s[window_start:window_end + 1]:
            if char in vs:
                count += 1

        max_v = max(max_v, count)

        while window_end < len(s):

            if s[window_start] in vs:
                count -= 1

            if window_end + 1  == len(s):
                break
            elif s[window_end + 1] in vs:
                count += 1

            max_v = max(max_v, count)
            window_start += 1
            window_end += 1

        return max_v
