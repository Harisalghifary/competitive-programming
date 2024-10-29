# Difficulty : Medium
# Tag : Dynamic Programming, dfs, array
def maxMoves(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0]* cols for _ in range(rows)]

    for j in range(cols-2,-1,-1):
        for i in range(rows-1, -1, -1):
            # print('i',i,j)
            curr = grid[i][j]
            # check down
            if (i < rows-1):
                if curr < grid[i+1][j+1]:
                    dp[i][j] = max(dp[i][j], dp[i+1][j+1]+1)
            # check samping
            if curr < grid[i][j+1]:
                dp[i][j] = max(dp[i][j], dp[i][j+1]+1)
            # check up
            if (i > 0):
                if curr < grid[i-1][j+1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j+1]+1)

    # print('dp',dp)
    res = 0
    for i in range(rows):
        # print(i)
        res = max(res, dp[i][0])

    return res

    