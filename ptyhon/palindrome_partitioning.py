def partition(self, s: str):
    res = []
    sub = []

    def is_palindrome(s):
        if s == s[::-1]:
            return True
        return False

    def dfs(inx):
        if inx >= len(s):
            res.append(sub.copy())
            return
        rest = s[inx:]
        for i in range(len(rest)):
            substr = rest[: i + 1]
            if is_palindrome(substr):
                sub.append(substr)
                dfs(inx + len(substr))
                sub.pop()

    dfs(0)

    return res
