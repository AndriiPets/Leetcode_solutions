def characterReplacement(s: str, k: int) -> int:
    length = len(s) - 1
    left = 0
    right = 0
    count = 0
    d = {}

    def check_d(string):
        if max(d.values()) >= len(string) - k:
            return True
        return False

    while right <= length:
        string = s[left : right + 1]
        if not d.get(s[right]):
            d[s[right]] = 1

        if check_d(string):
            if len(string) >= count:
                count = len(string)

            right += 1
            if right <= length and d.get(s[right]):
                d[s[right]] += 1

        else:
            d[s[left]] -= 1
            left += 1

    return count
