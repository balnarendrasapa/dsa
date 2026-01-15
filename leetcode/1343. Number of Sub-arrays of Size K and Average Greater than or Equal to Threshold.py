class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        runningSum = sum(arr[:k])

        result = 1 if runningSum / k >= threshold else 0

        for i in range(k, len(arr)):

            runningSum -= arr[i - k]
            runningSum += arr[i]

            if runningSum / k >= threshold:
                result += 1

        return result
