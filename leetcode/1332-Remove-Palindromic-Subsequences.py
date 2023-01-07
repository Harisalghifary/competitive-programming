def removePalindromeSub(self, s: str) -> int:
    left, right = 0, len(s)-1
    while right>=left:
        if s[left]!=s[right]:
            return 2
        left+=1
        right-=1
    return 1