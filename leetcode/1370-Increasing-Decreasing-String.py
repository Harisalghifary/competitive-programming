from collections import Counter
def sortString(self, s: str) -> str:
    cnt = Counter(s)
    result = []
    while cnt:
        for i in string.ascii_lowercase, reversed(string.ascii_lowercase):
            result += [char for char in i if char in cnt]
            cnt -= dict.fromkeys(cnt,1)
    return "".join(result)