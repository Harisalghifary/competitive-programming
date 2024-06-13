# Difficulty : Medium
# Tag : string, greedy, two pointer
def appendCharacters(self, s: str, t: str) -> int:
    anchor = 0
    for i in range(len(s)):
        # return 0 if all char in t is in s 
        if anchor>=len(t):
            return 0
        # contract to move anchor/index
        if s[i]==t[anchor]:
            anchor+=1
    # get the remaining length as result
    # by reduce len(t) with curr index/anchor
    return len(t)-anchor