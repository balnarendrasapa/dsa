class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answers = []

        if len(s) > 12:
            return answers

        def helper(index, dots, curr):
            
            if dots > 3 and index == len(s):
                answers.append(curr[:-1])
                return

            if dots > 3:
                return

            for j in range(index, min(index + 3, len(s))):
                if int(s[index:j + 1]) <= 255 and (index == j or s[index] != "0"):
                    helper(j + 1, dots + 1, curr + s[index:j + 1] + ".")
            

        helper(0, 0, "")

        return answers
