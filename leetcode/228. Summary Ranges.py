class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []
        
        ranges = []
        left = 0
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                continue
            else:
                if nums[left] == nums[i - 1]:
                    ranges.append(f"{nums[left]}")
                else:
                    ranges.append(f"{nums[left]}->{nums[i - 1]}")
                left = i

        if left == len(nums) - 1:
            ranges.append(f'{nums[left]}')
        else:
            ranges.append(f'{nums[left]}->{nums[-1]}')

        return ranges
