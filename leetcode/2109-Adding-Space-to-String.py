# Difficulty : Medium
# Tag : two pointer, string
def addSpaces(self, s: str, spaces: List[int]) -> str:
    newString = []
    anchor = 0
    for space in spaces:
        newString.append(s[anchor:space])
        newString.append(" ")
        anchor = space

    newString.append(s[anchor:])
    return "".join(newString)