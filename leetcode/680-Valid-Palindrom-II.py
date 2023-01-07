def validPalindrome(self, s: str) -> bool:
    def isPalindrom(s:str) -> bool:
        left, right = 0, len(s)-1
        while right>=left:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

    left, right = 0, len(s)-1
    while right>=left:
        if s[left]!=s[right]:
            return isPalindrom(s[left+1:right+1]) or isPalindrom(s[left:right])
        else:
            left+=1
            right-=1
    return True