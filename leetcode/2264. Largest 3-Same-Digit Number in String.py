class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        count = 1
        good_num = float("-inf")
        start = float("inf")
        good_int = ""
        i = 0

        for i in range(1, len(num)):
            if num[i - 1] == num[i]:
                count += 1
                start = min(start, i - 1)
            else:
                if count >= 3:
                    if good_num < int(num[i - 1]):
                        good_num = max(good_num, int(num[i - 1]))
                        good_int = num[start:start + 3]

                start = i
                count = 1

        if i == len(num) - 1 and count >= 3:
            if good_num < int(num[i - 1]):
                good_num = max(good_num, int(num[i - 1]))
                good_int = num[start:start + 3]

        return good_int
