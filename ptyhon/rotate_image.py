def rotate(matrix) -> None:
    rows, cols = len(matrix) - 1, len(matrix[0]) - 1
    corners = [[0, 0], [0, cols], [cols, rows], [rows, 0]]
    c = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    dirs = {"right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0]}

    def add_l(l1, l2):
        return [
            [l1[i][j] + l2[i][j] for j in range(len(l1[0]))] for i in range(len(l1))
        ]

    def rot(mtx, up_left, up_right, low_right, low_left):
        if len(range(up_left[1], up_right[1])) < 1:
            return

        up_r_x, up_r_y = up_right[0], up_right[1]
        up_l_x, up_l_y = up_left[0], up_left[1]
        low_r_x, low_r_y = low_right[0], low_right[1]
        low_l_x, low_l_y = low_left[0], low_left[1]
        temp = 0

        for i in range(up_left[1], up_right[1]):
            temp = mtx[up_r_x][up_r_y]
            mtx[up_r_x][up_r_y] = mtx[up_l_x][up_l_y]
            mtx[up_l_x][up_l_y] = mtx[low_l_x][low_l_y]
            mtx[low_l_x][low_l_y] = mtx[low_r_x][low_r_y]
            mtx[low_r_x][low_r_y] = temp

            up_l_x, up_l_y = up_l_x + dirs["right"][0], up_l_y + dirs["right"][1]
            up_r_x, up_r_y = up_r_x + dirs["down"][0], up_r_y + dirs["down"][1]
            low_r_x, low_r_y = low_r_x + dirs["left"][0], low_r_y + dirs["left"][1]
            low_l_x, low_l_y = low_l_x + dirs["up"][0], low_l_y + dirs["up"][1]

        corners_r = add_l([up_left, up_right, low_right, low_left], c)
        if corners_r[0][1] < corners_r[1][1]:
            rot(mtx, *corners_r)

    rot(matrix, *corners)
