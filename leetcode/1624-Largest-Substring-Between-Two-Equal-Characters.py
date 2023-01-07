from collections import Counter
def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    s1 = set(s)
    if len(s)==len(s1):
        return -1
    cnt = Counter(s)
    max_result, current, length = 0, 0, len(s)-1
    left, right = 0, length

    while right>=left:
        if s[left] in cnt and cnt[s[left]]>1:
            while s[right]!=s[left]:
                right-=1
                continue
            current = right-left-1
            max_result = max(max_result, current)
            
        left+=1
        right=length
        
    return max_result