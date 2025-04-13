from typing import List

# see https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0

        num_rows = len(grid)            # y-len
        num_cols = len(grid[0])         # x-len

        visited: List[List[bool]] = [
            [False for _ in range(num_cols)] for _ in range(num_rows)]

        for i in range(num_rows):       # row
            for j in range(num_cols):   # col
                # check if hit
                if (grid[i][j] == "0"):
                    continue

                # skip already visited node
                if (visited[i][j] == True):
                    continue

                def check(x, y):
                    # base-case
                    if (x < 0 or x >= num_cols) or (y < 0 or y >= num_rows) or (grid[y][x] == "0" or (visited[y][x] == True)):
                        return

                    visited[y][x] = True

                    lft = x - 1
                    rgt = x + 1
                    btm = y + 1
                    top = y - 1

                    check(lft, y)
                    check(rgt, y)
                    check(x, btm)
                    check(x, top)

                check(j, i)
                num_islands += 1

        return num_islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution.numIslands(grid))  # Output: 3
