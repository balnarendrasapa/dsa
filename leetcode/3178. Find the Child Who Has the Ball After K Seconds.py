class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        
        i = 0
        op = 1
        while k != 0:
            i += op
            k -= 1
            if i == n - 1:
                op = -1
            
            if i == 0:
                op = 1
                

        return i
