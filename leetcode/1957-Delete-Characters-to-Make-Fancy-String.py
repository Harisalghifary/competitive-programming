# Difficulty : Easy
# Tag : string
def makeFancyString(self, s: str) -> str:
    if len(s)<3:
        return "".join([s[:2]])

    res = [s[0],s[1]]
    for i in range(2, len(s)):
        if s[i]!=res[-1] or s[i]!=res[-2]:
            res.append(s[i])

    return "".join(res)