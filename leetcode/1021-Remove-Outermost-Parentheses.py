def removeOuterParentheses(self, s: str) -> str:
    result = ""
    curr = 0
    for char in s:
        if char == "(":
            if curr>0:
                result += "("
            curr+=1

        elif char == ")":
            curr-=1
            if curr>0:
                result += ")"

    return result