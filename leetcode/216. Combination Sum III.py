class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        numbers = [1,2,3,4,5,6,7,8,9]

        result = []

        def backtrack(index, arr, sum_v):

            if sum_v == n and len(arr) == k:
                result.append(arr)
                return

            if len(arr) > k or index >= len(numbers):
                return 

            backtrack(index + 1, arr, sum_v)
            backtrack(index + 1, arr + [numbers[index]], sum_v + numbers[index])

        backtrack(0, [], 0)
        return result
