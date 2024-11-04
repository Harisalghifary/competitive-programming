# Difficulty: Medium
# Tag: backtrack, hashtable
def maxUniqueSplit(self, s: str) -> int:
    def backtrack(start, seen):
        if start == len(s):
            return 0

        maxSplit = 0
        for end in range(start+1, len(s)+1):
            target = s[start:end]
            if target not in seen:
                # process
                seen.add(target)
                maxSplit = max(maxSplit, 1+ backtrack(end, seen))
                seen.remove(target)

        return maxSplit
    
    return backtrack(0, set())