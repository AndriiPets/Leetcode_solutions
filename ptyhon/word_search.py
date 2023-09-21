def exist(self, board, word: str) -> bool:
    width = len(board[0])
    height = len(board)
    visited = set()

    def is_valid(row, col, inx):
        if row < 0 or col < 0 or row >= height or col >= width:
            return False
        if board[row][col] != word[inx] or (row, col) in visited:
            return False
        return True

    def dfs(r, c, i):
        if i == len(word):
            return True
        if not is_valid(r, c, i):
            return False

        visited.add((r, c))
        m = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        visited.remove((r, c))

        return m

    for row in range(height):
        for col in range(width):
            if dfs(row, col, 0):
                return True
    return False
