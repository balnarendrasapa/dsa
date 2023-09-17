class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            res = 0
            check = x
            while x != 0:
                last_digit = x % 10
                x_update = x // 10
                res = 10 * res + last_digit
                x = x_update

            if res == check:
                return True
