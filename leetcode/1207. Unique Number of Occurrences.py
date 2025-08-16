from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)

        track = set()

        for key in c.keys():
            if c[key] not in track:
                track.add(c[key])
            else:
                return False

        return True
