class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def stringify_sort(num):
            return "".join(sorted(str(num)))

        target = stringify_sort(n)

        for i in range(31):
            if stringify_sort(1 << i) == target:
                return True

        return False
