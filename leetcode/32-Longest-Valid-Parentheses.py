def longestValidParentheses(self, s: str) -> int:
    result, left, right = 0, 0, 0
    len_s = len(s)

    for idx, char in enumerate(s):
        if char == ")":
            right+=1
        elif char == "(":
            left+=1
        
        if left==right:
            result = max(result, left+right)
        elif right>=left:
            left, right = 0, 0

    left, right = 0, 0
    for i in range(len_s-1, -1,-1):
        if s[i] == "(":
            left+=1
        elif s[i] ==")":
            right+=1

        if left==right:
            result = max(result, left+right)
        elif left>=right:
            left, right = 0, 0
            
    return result