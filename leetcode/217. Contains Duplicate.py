class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track = dict()
        for i in nums:
            try:
                track[i] += 1
            except:
                track[i] = 1
        for key, value in track.items():
            if value > 1:
                return True
        return False
        
        
