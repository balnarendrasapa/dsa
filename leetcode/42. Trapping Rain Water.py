class Solution:
    def trap(self, height: List[int]) -> int:
        
        max1 = []
        temp = 0
        for i in height:
            if temp < i:
                temp = i
            max1.append(temp)

        max2 = []
        temp = 0
        for i in height[::-1]:
            if temp < i:
                temp = i
            max2.append(temp)  

        max2.reverse()

        water = []
        for i in range(len(height)):
            if i == 0:
                water.append(0)
                continue
            
            m1 = max1[i]
            m2 = max2[i]

            if height[i] > m1 or height[i] > m2:
                water.append(0)
                continue
                
            water.append(min(m1, m2) - height[i])

        return sum(water)
