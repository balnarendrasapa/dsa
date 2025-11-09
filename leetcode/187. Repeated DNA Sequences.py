class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = defaultdict(int)

        for i in range(len(s)):
            t = s[i:i + 10]
            result[t] += 1

        R = []
        for key in result.keys():
            if result[key] > 1:
                R.append(key)

        return R
