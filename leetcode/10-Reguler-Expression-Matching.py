# Difficulty: Hard
# Tag: string, dynamic programming, Recursion
def isMatch(self, s: str, p: str) -> bool:
    # using cache with maps
    cache = {}

    # TOP-Down recursive
    def dfs(i,j):
        # check cache
        if (i,j) in cache:
            return cache[(i,j)]
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
            cache[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))
            return cache[(i,j)]
        # handle for case . and letter
        if match:
            cache[(i,j)] = dfs(i+1,j+1)
            return cache[(i,j)]

        cache[(i,j)] = False
        return False

    # call dfs
    return dfs(0,0)