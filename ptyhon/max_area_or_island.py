from collections import deque


def maxAreaOfIsland(self, grid) -> int:
    cols = len(grid[0])
    rows = len(grid)
    visited = set()
    islands_max_area = 0

    def is_valid(r, c):
        if (
            r in range(rows)
            and c in range(cols)
            and grid[r][c] == 1
            and (r, c) not in visited
        ):
            return True
        return False

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited.add((r, c))
        area = 1

        while q:
            row, col = q.popleft()
            dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dr, dc in dirs:
                xr = row + dr
                xc = col + dc
                if is_valid(xr, xc):
                    q.append((xr, xc))
                    visited.add((xr, xc))
                    area += 1
        return area

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                area = bfs(i, j)
                if area > islands_max_area:
                    islands_max_area = area

    return islands_max_area
