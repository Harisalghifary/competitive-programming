# Difficulty : Easy
# Tag : Two pointers, string, daily leetcode challenge 18 April 2023

def mergeAlternately(self, word1: str, word2: str) -> str:
    # word1 and word2
    # if word.length > other, append the remain to the end
    # append word1[i], word2[i]
    # if len w1>w2: append until len(w2), append remaining w1 to result.
    # if len w2>w1: otherwise
    # if len w1==w2: append 
    result = ""
    def helper(shortLength):
        merged = ""
        for i in range(shortLength):
            merged+=(word1[i])
            merged+=(word2[i])
        return merged
    if len(word1)!=len(word2):
        if len(word1)>len(word2):
            merged = helper(len(word2))
            result+= merged + (word1[len(word2):])

        else:
            merged = helper(len(word1))
            result+= merged + (word2[len(word1):])

    else:
        result += helper(len(word1))

    return result