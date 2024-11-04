# Difficulty : Medium
# Tag : string
def compressedString(self, word: str) -> str:
    if len(word)==1:
        return "1"+word[0]

    res = []
    length = 1
    for i in range(1,len(word)):
        curr = word[i]
        if curr != word[i-1]:
            res.append(f"{min(length,9)}{word[i-1]}")
            length = 1
        else:
            length +=1

        if length > 9:
            res.append("9"+word[i-1])
            length = 1
    if length>0:
        res.append(f"{length}{word[-1]}")
    return "".join(res)