class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0
        neg = False
        if x < 0:
            x = -x
            neg = True
        while x != 0:
            if res < INT_MIN or res > INT_MAX:
                return 0
            last_digit = x % 10
            x_update = x // 10
            res = 10 * res + last_digit
            x = x_update
        if neg == True:
            res = -res
        if res < INT_MIN or res > INT_MAX:
            return 0
        return res
