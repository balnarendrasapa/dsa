mem = {}

class Solution:
    def countDigitOne(self, n: int) -> int:
        if n in mem:
            return mem[n]
            
        if n <= 0:
            return 0
        if n < 10:
            return 1 if n >= 1 else 0

        sn = str(n)
        first_digit = int(sn[0])
        rest = int(sn[1:]) if len(sn) > 1 else 0
        power = 10 ** (len(sn) - 1)

        if first_digit > 1:
            first_count = power
        else:
            first_count = rest + 1

        other_count = first_digit * self.countDigitOne(power - 1)

        rest_count = self.countDigitOne(rest)

        mem[n] = first_count + other_count + rest_count
        return mem[n]
