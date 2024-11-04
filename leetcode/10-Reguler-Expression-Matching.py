# Difficulty: Hard
# Tag: string, dynamic programming, Recursion
def isMatch(self, s: str, p: str) -> bool:
    # TOP-Down recursive
    def dfs(i,j):
        # base case
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False

        # case . and letter
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        # handle *
        if (j+1)<len(p) and p[j+1] == '*':
            # handle for empty (i,j+2) and consecutive (i+1,j)
            return dfs(i,j+2) or (match and dfs(i+1,j))
        # handle for case . and letter
        if match:
            return dfs(i+1,j+1)

        return False

    # call dfs
    return dfs(0,0)
    