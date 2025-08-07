class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        not_rotten = 0
        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    not_rotten += 1

        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        current_rotten = [(i, j) for i in range(rows) for j in range(columns) if grid[i][j] == 2]
        while not_rotten > 0:
            temp_indices = []
            for i, j in current_rotten:
                for dx, dy in directions:
                    if 0 <= i + dx < rows and 0 <= j + dy < columns and grid[i + dx][j + dy] == 1:
                        grid[i + dx][j + dy] = 2
                        not_rotten -= 1
                        temp_indices.append((i + dx, j + dy))

            if len(temp_indices) == 0:
                break

            current_rotten = temp_indices

            minutes += 1

        if not_rotten > 0:
            return -1

        return minutes
