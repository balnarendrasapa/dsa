class Solution:
    def merge(self, a, b):
        i = j = 0
        merged = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1

        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    def mergesort(self, nums, i, j):
        if i == j:
            return [nums[i]]

        mid = (i + j) // 2
        a = self.mergesort(nums, i, mid)
        b = self.mergesort(nums, mid + 1, j)
        return self.merge(a, b)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return self.mergesort(nums, 0, n - 1)
