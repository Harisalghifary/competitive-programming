# Difficulty : Medium
# Tag : Set, string, hash table
def countPalindromicSubsequence(self, s: str) -> int:
    uniqSet = set(s)
    res = 0
    for char in uniqSet:
        left, right = s.find(char), s.rfind(char)
        if right > left+1:
            # ensure that there is element in middle
            res += len(set(s[left+1:right]))

    return res