class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        less_than = [asteroids[i] for i in range(len(asteroids)) if asteroids[i] <= mass]
        more_than = [asteroids[i] for i in range(len(asteroids)) if asteroids[i] > mass]

        less_than.sort(key = lambda x: -x)
        more_than.sort()

        for l in less_than:
            mass += l

        for m in more_than:
            if mass >= m:
                mass += m
            else:
                return False

        return True
