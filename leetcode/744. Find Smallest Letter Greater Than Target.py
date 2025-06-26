class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters)
        while start < end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid
        
        return letters[start % len(letters)]
