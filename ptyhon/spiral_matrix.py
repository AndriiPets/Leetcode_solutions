def spiralOrder(matrix):
    res = []
    path = {}
    width = len(matrix[0])
    height = len(matrix)

    Rows = [0, 1, 0, -1]
    Cols = [1, 0, -1, 0]

    def is_valid(row, col):
        if (
            row < 0
            or col < 0
            or row >= height
            or col >= width
            or (row, col) in path.keys()
        ):
            return False
        return True

    def traverse(r, c):
        if not is_valid(r, c):
            return

        res.append(matrix[r][c])
        path[(r, c)] = 1
        row, col = r, c
        d = (r, c)
        for i in range(0, 4):
            row = d[0] + Rows[i]
            col = d[1] + Cols[i]
            while is_valid(row, col):
                d = (row, col)
                path[(row, col)] = 1
                res.append(matrix[row][col])
                row += Rows[i]
                col += Cols[i]
        traverse(row + 1, col + 1)

    traverse(0, 0)

    return res
