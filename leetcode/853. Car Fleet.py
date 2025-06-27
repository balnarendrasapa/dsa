class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]

        answer = 0

        while len(times) > 1:
            # print(times)
            lead = times.pop()
            if lead < times[-1]:
                answer += 1
            else:
                times[-1] = lead

        return answer + bool(times)

        return 1
