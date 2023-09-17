class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        temp = [[] for i in range(numRows)]
        
        index = 0
        step = 0
        for i in range(len(s)):
            temp[index].append(s[i])
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        resultant = ''
        for i in temp:
            j = ''.join(i)
            resultant += j
        return resultant
