def reverseOnlyLetters(self, s: str) -> str:

    left, right = 0, len(s)-1
    s = list(s)
    while left<right:
        if s[left].isalpha() and s[right].isalpha():
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        elif s[left].isalpha():
            right-=1
        elif s[right].isalpha():
            left+=1
        else:
            left+=1
            right-=1
    return "".join(s)                