class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        fo = -1
        arr = nums
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                fo = mid
                end = mid - 1
            elif arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1

        start = 0
        end = len(nums) - 1
        lo = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                lo = mid
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1

        return [fo, lo]
