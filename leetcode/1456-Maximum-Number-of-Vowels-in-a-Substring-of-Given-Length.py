# Difficulty : Medium
# Tag : Sliding Window, String
def maxVowels(self, s: str, k: int) -> int:
    vowel = {"a","i","u","e","o"}
    curr = 0
    for i in range(k):
        if s[i] in vowel:
            curr+=1
    
    left,right = 0, k
    maxVowelCount = curr
    while right<len(s):
        # expand the window 
        if s[right] in vowel:
            curr+=1
        if s[left] in vowel:
            curr-=1
        # Process the window
        # compare curr with global max
        maxVowelCount = max(maxVowelCount, curr)
        # move sliding window
        left+=1
        right+=1

    return maxVowelCount