import bisect

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        number = str(n)
        base = len(digits)

        result = 0
        for i in range(1, len(number)):
            result += pow(base, i)

        j = 0
        temp = len(number) - 1
        while j < len(number):
            elems = bisect.bisect_left(digits, number[j])
            result += elems * pow(base, temp)
            if elems < len(digits) and digits[elems] == number[j]:
                j += 1
                temp -= 1
            else:
                return result

        return result + 1
