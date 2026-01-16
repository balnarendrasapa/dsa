class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        resultantReleases = [releaseTimes[0]]

        for i in range(1, len(releaseTimes)):
            resultantReleases.append(releaseTimes[i] - releaseTimes[i - 1])

        releaseTuples = [(keysPressed[i], resultantReleases[i]) for i in range(len(releaseTimes))]

        releaseTuples.sort(key = lambda x: (x[1], x[0]))

        return releaseTuples[-1][0]
