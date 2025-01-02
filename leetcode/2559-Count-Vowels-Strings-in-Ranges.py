# Difficulty : Medium
# Tag : Array, prefix sum
def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    prefixArr = [0] * (len(words)+1)
    vowels = {"a","i","u","e","o"}
    def isAnyVowel(s):
        return s[0] in vowels and s[-1] in vowels

    for i,word in enumerate(words):
        curr = isAnyVowel(word)
        if curr:
            prefixArr[i+1]=prefixArr[i] + 1
        else:
            prefixArr[i+1]=prefixArr[i]
    
    res = []
    for q in queries:
        curr = prefixArr[q[1]+1] - prefixArr[q[0]]
        res.append(curr)

    return res