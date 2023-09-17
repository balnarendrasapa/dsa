class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = 999
        for i in strs:
            if min > len(i):
                min = len(i)
        k = 0
        left = 0
        index = 0
        flag = False
        while left < min:
            for i in range(len(strs)):
                print(index, left)
                if strs[index][left] != strs[i][left]:
                    flag = True
            left += 1 
            if flag == False:
                k += 1
            else:
                break
        return strs[0][:k]
