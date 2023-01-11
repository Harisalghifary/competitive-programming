# Easy Difficulty
# Tag : Two Pointers, String 
def reverseStr(self, s: str, k: int) -> str:
    if k == 1:
        return s
    def reverse(l, r):
        while l<r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        return

    count, n = 0, len(s)
    s = list(s)
    # two pointer
    # with left and right as pointer
    # state as state if string is reverse or not
    left, right, state = 0,0,0
    while right<n:
        right= (right+k-1)
        if right>=n:
            right=n-1
        if state%2==0:
            reverse(left,right)
        right+=1
        left=right
        state+=1
    return "".join(s)