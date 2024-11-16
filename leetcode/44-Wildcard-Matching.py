# Difficulty : Hard
# Tag : String, dynamic programming, greedy, recursion
def isMatch(self, s: str, p: str) -> bool:
    @lru_cache(None)
    def dfs(i,j):
        # base case
        if j == len(p):
            # return True if i == len(s)
            return i == len(s)

        # handle *
        # * -> any sequence
        if p[j] == '*':
            return dfs(i,j+1) or (i < len(s) and dfs(i+1,j))
        # logic match
        match = i < len(s) and (s[i]==p[j] or p[j]=='?')
        if match:
            return dfs(i+1,j+1)

        return False
    
    return dfs(0,0)
        