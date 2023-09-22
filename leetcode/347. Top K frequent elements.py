class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            try:
                count[i] += 1
            except:
                count[i] = 1

        res = [k for k, v in sorted(count.items(), key = lambda item: item[1], reverse = True)]

        return res[:k]
        
