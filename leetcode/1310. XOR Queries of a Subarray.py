class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = []

        temp = 0
        for i in arr:
            temp = temp ^ i
            prefix_xor.append(temp)

        result = []

        for i in queries:
            if i[0] == 0:
                result.append(prefix_xor[i[1]])
                continue
            result.append(prefix_xor[i[1]] ^ prefix_xor[i[0] - 1])

        return result
