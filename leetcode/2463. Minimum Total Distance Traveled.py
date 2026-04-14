from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        @lru_cache(maxsize = None)
        def dp(i, j, used):
            if i == len(robot):
                return 0
            if j == len(factory):
                return float("inf")

            position, capacity = factory[j]

            result = dp(i, j + 1, 0)

            if used < capacity:
                result = min(result, abs(robot[i] - position) + dp(i + 1, j, used + 1))

            return result

        return dp(0, 0, 0)
