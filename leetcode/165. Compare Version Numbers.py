class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        for rev_one, rev_two in zip_longest(v1, v2, fillvalue = 0):
            if rev_one == rev_two:
                continue

            return -1 if rev_one < rev_two else 1

        return 0
