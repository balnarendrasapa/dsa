class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def getParenthesis(par, o, c):
            if len(par) == 2 * n:
                ans.append(par)
                return

            if o < n:
                getParenthesis(par + "(", o + 1, c)
            
            if c < o:
                getParenthesis(par + ")", o, c + 1)

        getParenthesis("", 0, 0)
        return ans
