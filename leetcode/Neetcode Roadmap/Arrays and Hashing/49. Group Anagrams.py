class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = [[] for i in strs]
        strings = []
        dic = dict()
        k = 0
        strs2 = []
        var = 0

        for i in strs:
            if i == "":
                k += 1
                continue
            strs2.append(i)
            strings.append("".join(sorted(i)))

        for i in strings:
            var += 1
            dic[i] = var

        group = []
        for i in strings:
            group.append(dic[i])

        result = dict()
        for i in range(len(group)):
            try:
                result[group[i]].append(strs2[i])
            except:
                result[group[i]] = [strs2[i]]

        res = list(result.values())
        if k > 0:
            res.append([""]*k)

        return res
        
