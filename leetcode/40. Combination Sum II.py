class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        results = []

        def backtrack(index, arr, sum_v):
            if index > len(candidates) or sum_v > target:
                return

            if sum_v == target:
                results.append(arr)
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                backtrack(i + 1, arr + [candidates[i]], sum_v + candidates[i])

        backtrack(0, [], 0)
        return results
