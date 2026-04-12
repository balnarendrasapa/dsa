from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_distance(a, b):
            if a == 26 or b == 26:
                return 0

            a1, a2 = divmod(a, 6)
            b1, b2 = divmod(b, 6)

            return abs(a1 - b1) + abs(a2 - b2)

        @lru_cache(None)
        def get_min_dist(idx, f1, f2):
            if idx == len(word):
                return 0

            curr = ord(word[idx]) - ord("A")

            f1_dist = get_distance(f1, curr) + get_min_dist(idx + 1, curr, f2)

            f2_dist = get_distance(f2, curr) + get_min_dist(idx + 1, f1, curr)

            return min(f1_dist, f2_dist)

        return get_min_dist(0, 26, 26)
