from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        mapping = {}
        count = 0

        for hour in hours:
            rem = hour % 24
            complmnt = (24 - rem) % 24

            if complmnt in mapping:
                count += mapping[complmnt]
            
            mapping[rem] = mapping.get(rem, 0) + 1
        
        return count
