class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        max_v = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_v:
                result.append(True)
            else:
                result.append(False)

        return result
