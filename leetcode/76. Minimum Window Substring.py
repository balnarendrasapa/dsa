from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        if len(s) < len(t):
            return ""

        if not s or not t:
            return ""

        t_char = Counter(t)
        required = len(t_char)

        left, right = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in t_char and window_counts[char] == t_char[char]:
                formed += 1

            while left <= right and required == formed:
                char = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_counts[char] -= 1
                if char in t_char and window_counts[char] < t_char[char]:
                    formed -= 1

                left += 1

            right += 1

        if ans[0] == float("inf"):
            return ""
        else:
            return s[ans[1]:ans[2] + 1]
        
