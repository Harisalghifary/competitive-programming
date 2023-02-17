# Difficulty : Medium
# Tag : string, hash table, sliding window
def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    # edge case
    if minSize>len(s):
        return 0
    # Define variable
    dictSubString = {}
    left, right = 0, minSize
    maxOcc = 0
    # iterate over input
    while right<=len(s):
        x = s[left:right]
        # stop condition
        if len(set(x))<=maxLetters:
            dictSubString[x] = dictSubString.get(x,0)+1
            curr = dictSubString[x]
            # process current window
            maxOcc = max(curr, maxOcc)
        left+=1
        right+=1
    return maxOcc