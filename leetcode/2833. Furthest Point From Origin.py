from collections import Counter

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d = Counter(moves)
        
        return d["_"] + abs(d["L"] - d["R"])
