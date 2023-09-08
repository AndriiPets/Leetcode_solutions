def letterCombinations(digits: str):
    if not digits:
        return []
    res = []
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(s, inx):
        if inx >= len(digits):
            res.append(s)
            return
        num = keyboard[digits[inx]]
        for i in num:
            dfs(s + i, inx + 1)

    dfs("", 0)

    return res
