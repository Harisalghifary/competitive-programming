def reverseWords(self, s: str) -> str:
    def reverse(left, right):
        while left<right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return
    left, right, n = 0,0,len(s)
    s = list(s)
    while right<n:
        if s[right]==' ':
            reverse(left,right-1)
            right+=1
            left = right
            continue
        right+=1
    reverse(left, right-1)

    return "".join(s)