class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        k = 0
        temp = []

        for i in s:
            if i not in temp :
                k += 1
                temp.append(i)
            else:
                index = temp.index(i)
                temp = temp[index + 1 :]
                k = len(temp)
                temp.append(i)
                k +=1
            if k >= max:
                max = k
        
        return max
        
