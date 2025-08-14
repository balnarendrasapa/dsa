import bisect
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        p_len = len(potions)
        result = []

        for spell in spells:
            target = math.ceil(success / spell)
            
            left, right = 0, len(potions)
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            result.append(p_len - left)

        return result
