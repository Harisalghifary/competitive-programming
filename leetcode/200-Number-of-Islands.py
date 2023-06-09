# Difficulty : Mediium
# Tag : array, dfs, bfs, Union-find, matrix
def numIslands(self, grid: List[List[str]]) -> int:
    result = 0
    # DFS Method
    # x -> row
    # y -> column
    def dfs(x,y):
        # check out bound
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y] != "1" : return
        # mark visited
        grid[x][y] = "#"
        # explore all neighbour
        dfs(x+1,y) # up
        dfs(x-1,y) # down
        dfs(x, y+1) # right
        dfs(x, y-1) # left

    # iterate toward until find '1'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":
                result += 1
                dfs(i,j)

    return result