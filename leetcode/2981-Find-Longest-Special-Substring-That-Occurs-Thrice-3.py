# Difficulty : Medium
# Tag: Two pointer, binary search, hash table
def maximumLength(self, s: str) -> int:
    n = len(s)
    maps = {}

    for i in range(n):
        subString = ""
        for j in range(i, n):
            subString += s[j]
            # special
            if len(set(subString)) == 1:
                maps[subString] = maps.get(subString, 0)+1

    res = -1
    for key, val in maps.items():
        if val>=3:
            res = max(res, len(key))

    return res