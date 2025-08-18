from itertools import permutations

class Solution:
    def check(self, cards, target = 24):
        if len(cards) == 1:
            return abs(cards[0] - target) < 1e-6

        for a, b in permutations(cards, 2):
            temp = [a + b, a - b, a * b]
            if b > 1e-6:
                temp.append(a / b)
            nc = cards[:]
            nc.remove(a)
            nc.remove(b)
            for t in temp:
                if self.check(nc + [t], target):
                    return True

        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        return self.check(cards)
