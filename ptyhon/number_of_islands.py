from collections import deque


def numIslands(self, grid: List[List[str]]) -> int:
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]
    width = len(grid[0])
    height = len(grid)
    islands = 0

    def is_valid(row, col):
        if row < 0 or col < 0 or row >= height or col >= width:
            return False
        if grid[row][col] == "0" or grid[row][col] == "v":
            return False
        return True

    def bfs(row, col):
        q = deque()
        q.append((row, col))
        grid[row][col] = "v"

        while q:
            cell = q.popleft()
            x = cell[0]
            y = cell[1]

            for i in range(4):
                xrow = x + dRow[i]
                xcol = y + dCol[i]
                if is_valid(xrow, xcol):
                    q.append((xrow, xcol))
                    grid[xrow][xcol] = "v"

    for i in range(height):
        for j in range(width):
            if grid[i][j] == "1":
                bfs(i, j)
                islands += 1

    return islands
