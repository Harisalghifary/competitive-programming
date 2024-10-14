# Difficulty : Medium
# Tag: stack, string
def minAddToMakeValid(self, s: str) -> int:
    stack = []
    count = 0
    for ch in s:
        if ch == ')':
            # process
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                count +=1
        else:
            stack.append(ch)
    return count + len(stack)