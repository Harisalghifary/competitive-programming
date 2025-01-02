# Difficulty : Easy
# Tag: Array
def maxScore(self, s: str) -> int:
    res = countOnes = countZeros = 0
    for char in s:
        if char == "1":
            countOnes+=1

    for i in range(len(s)-1):
        if s[i] == "0":
            countZeros+=1
        else:
            countOnes-=1

        res = max(res, countZeros+countOnes)
    
    return res