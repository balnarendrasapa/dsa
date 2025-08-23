class Solution:
    def getTrees(self, min_val, max_val, memo):
        if (min_val, max_val) in memo:
            return memo[(min_val, max_val)]

        if min_val >= max_val:
            return 1

        bst_count = 0
        for val in range(min_val, max_val + 1):
            l = self.getTrees(min_val, val - 1, memo)
            r = self.getTrees(val + 1, max_val, memo)

            bst_count += l * r

        memo[(min_val, max_val)] = bst_count

        return bst_count
        
    def numTrees(self, n: int) -> int:
        return self.getTrees(1, n, {})
