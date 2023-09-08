def generateParenthesis(self, n: int):
    res = []
    count = n

    def pairs(s, left, right):
        if left == 0 and right == 0:
            res.append(s)
            return

        if left:
            pairs(s + "(", left - 1, right)

        if right > left:
            pairs(s + ")", left, right - 1)

    pairs("", count, count)

    return res
