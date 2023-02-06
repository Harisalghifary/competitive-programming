# Difficulty : Medium
# Tag : Hash table, array, sliding window
def numberOfSubstrings(self, s: str) -> int:
    left, right = 0, 0
    countResult = 0
    # iterate backward
    dictOccurence = {'a':0, 'b':0, 'c':0}
    while right<len(s):
        dictOccurence[s[right]]+=1
        # contract windows
        while dictOccurence['a']>0 and dictOccurence['b']>0 and dictOccurence['c']>0:
            # proccess the current window
            countResult+=1
            dictOccurence[s[left]]-=1
            left+=1
            countResult+=len(s)-right-1
        # expand window
        right+=1
    return countResult