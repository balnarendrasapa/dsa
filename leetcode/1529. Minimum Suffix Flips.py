class Solution:
    def minFlips(self, target: str) -> int:
        
        flips = 0
        current_bit = "0"

        for char in target:

            if char != current_bit:
                flips += 1

                current_bit = '0' if current_bit == '1' else '1'

        return flips
