class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start, end = 0, len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][0] < target:
                start = mid + 1

        start1, end1 = 0, len(matrix[0]) - 1

        while start1 <= end1:
            mid = (start1 + end1) // 2
            if matrix[end][mid] == target:
                return True
            elif matrix[end][mid] > target:
                end1 = mid - 1
            elif matrix[end][mid] < target:
                start1 = mid + 1

        return False
