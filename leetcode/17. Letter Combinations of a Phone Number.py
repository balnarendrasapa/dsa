class Solution:
    def getCombinations(self, digits, num):
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return list(self.phone[digits[num]])

        if num == len(digits) - 1:
            return self.phone[digits[num]]

        result = []
        for char in self.phone[digits[num]]:
            arr = self.getCombinations(digits, num + 1)
            for a in arr:
                result.append(char + a)

        return result

    def letterCombinations(self, digits: str) -> List[str]:
        self.phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz" 
        }

        return self.getCombinations(digits, 0)
