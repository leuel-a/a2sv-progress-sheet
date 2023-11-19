class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_bound(row: int, col: int) -> bool:
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def findPerimeter(row: int, col: int) -> None:
            nonlocal perimeter
            visited.add((row, col))

            for r_inc, c_inc in directions:
                new_row, new_col = row + r_inc, col + c_inc

                if not in_bound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                    continue
                
                if (new_row, new_col) not in visited:
                    findPerimeter(new_row, new_col)

        visited, perimeter = set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    findPerimeter(i, j)
        return perimeter