# Difficulty : Easy
# Tag : Sliding window, hash table, array, string
from collections import Counter
def countGoodSubstrings(self, s: str) -> int:
    # Define variable
    left, right = 0, 2
    countResult = 0
    # Set stop condition
    while right<len(s):
        curr = len(Counter(s[left:right+1]))
        # Contract the window
        if curr==3:
            countResult+=1
        left+=1
        right+=1
    return countResult