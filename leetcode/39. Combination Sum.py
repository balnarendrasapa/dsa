class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        if target == 0:
            return [[]]

        if candidates[0] > target:
            return []

        result = []
        for i in range(len(candidates)):
            e = candidates[i]
            c = self.combinationSum(candidates[i:], target - e)
            for j in c:
                result.append([e] + j)

        return result


