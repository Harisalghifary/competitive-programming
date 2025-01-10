# Difficulty : Medium
# Tag: Hash table, array
def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    # counter for words2
    # check each word to word2 counter
    freq = {}
    for word in words2:
        curr = Counter(word)
        for key, val in curr.items():
            if key not in freq:
                freq[key] = val
            else:
                freq[key] = max(freq.get(key,0), val)
    
    def isSubset(w1):
        for key, val in freq.items():
            if key not in w1:
                return False
            elif val>w1[key]:
                return False
        return True

    res = []
    for word in words1:
        curr = Counter(word)
        isValid = isSubset(curr)
        if isValid:
            res.append(word)

    return res