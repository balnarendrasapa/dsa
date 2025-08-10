import bisect

class Solution:
    # Precompute specials ONCE for all test cases
    _special_nums_cache = None

    def subsets_at_most_one_odd(self, nums):
        n = len(nums)
        total_masks = 1 << n
        result = []

        for mask in range(total_masks):
            subset = []
            odd_count = 0
            valid = True

            for i in range(n):
                if mask & (1 << i):
                    if int(nums[i][0]) % 2 == 1: 
                        odd_count += 1
                        if odd_count > 1:
                            valid = False
                            break
                    subset.append(nums[i])

            if valid and sum(len(x) for x in subset) <= 8:
                result.append(subset)

        return result

    def generate_permutations(self, nums):
        result = []
        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + remaining[i], remaining[:i] + remaining[i+1:])
        backtrack("", nums)
        return result

    def getSpecials(self, sets):
        result = []
        for subset in sets:
            if not subset:
                continue
            odd_string = ""
            temp = ""
            for numset in subset:
                if int(numset[0]) % 2 == 1:
                    odd_string += numset[0]
                temp += numset[0] * (int(numset[0]) // 2)

            for permutation in self.generate_permutations(temp):
                k = int(permutation + odd_string + permutation[::-1])
                result.append(k)
        return result

    def _precompute_special_nums(self):
        nums = [['1']]
        for i in range(2, 10):
            temp = [str(i)] * (i // 2)
            nums.append(temp)
        subsets = self.subsets_at_most_one_odd(nums)
        specials = self.getSpecials(subsets)
        specials = sorted(set(specials)) 
        return specials

    def specialPalindrome(self, n: int) -> int:
        if Solution._special_nums_cache is None:
            Solution._special_nums_cache = self._precompute_special_nums()

        special_nums = Solution._special_nums_cache
        idx = bisect.bisect_right(special_nums, n)
        return special_nums[idx] if idx < len(special_nums) else -1
