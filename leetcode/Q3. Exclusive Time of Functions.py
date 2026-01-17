class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        transform = lambda log: (int(log[0]), log[1], int(log[2]))

        logs = [transform(log.split(":")) for log in logs]

        ans, s = [0] * n, []

        for (i, status, timestamp) in logs:
            if status == "start":
                if s: ans[s[-1][0]] += timestamp - s[-1][1]
                s.append([i, timestamp])
            else:
                ans[i] += timestamp - s.pop()[1] + 1
                if s: s[-1][1] = timestamp + 1

        return ans
