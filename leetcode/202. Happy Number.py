def getHappy(n):
    temp = 0
    for i in str(n):
        temp += int(i) ** 2

    return temp

def iHappy(n, seen=None):
    if seen is None:
        seen = set()

    if n == 1:
        return True

    if n not in seen:
        seen.add(n)
        return iHappy(getHappy(n), seen)
    
    return False

class Solution:
    def isHappy(self, n: int) -> bool:

        return iHappy(n)

        
