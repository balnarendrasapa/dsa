class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1

        check_set = set()
        remainder = 0
        test = "1"

        while True:
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return len(test)

            if remainder in check_set:
                return -1

            check_set.add(remainder)
            test = test + "1"
