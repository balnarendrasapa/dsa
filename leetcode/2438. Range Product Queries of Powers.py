class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        bin_num = bin(n)[2:]
        length = len(bin_num) - 1
        MOD = 10 ** 9 + 7

        powers = [length - i for i in range(len(bin_num)) if bin_num[i] != '0'][::-1]

        result = []
        for query in queries:
            result.append(pow(2, sum(powers[query[0]:query[1] + 1]), MOD))

        return result

        
