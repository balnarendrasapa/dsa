class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        size = 0

        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1

        for ch in reversed(s):
            k %= size

            if ch.isdigit():
                size //= int(ch)
            else:
                if k == 0:
                    return ch
                size -= 1
