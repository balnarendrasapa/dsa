class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]

        result = self.grayCode(n - 1)

        temp = []
        for i in reversed(result):
            temp.append((1 << (n - 1)) | i)

        return result + temp

        
