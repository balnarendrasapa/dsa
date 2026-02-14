class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        r = [[tickets[i], i] for i in range(len(tickets))]

        q = deque(r)
        t = 0
        while True:
            p = q.popleft()
            t += 1
            p[0] -= 1

            if p[0] == 0 and p[1] == k:
                return t
            else:
                if p[0] != 0:
                    q.append(p)
