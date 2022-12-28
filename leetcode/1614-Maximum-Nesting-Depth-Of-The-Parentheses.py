def maxDepth(self, s: str) -> int:
    result = 0
    curr = 0
    for char in s:
        if char == "(":
            curr += 1
            result = max(result, curr)
        elif char == ")":
            curr -= 1
    return result