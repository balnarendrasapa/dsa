class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        max_v = 0
        area = None
        for length, width in dimensions:
            length_of_diagonal = (length ** 2 + width ** 2) ** 0.5

            if length_of_diagonal > max_v or (length_of_diagonal == max_v and length * width > area):
                max_v = length_of_diagonal
                area = length * width

        return area
