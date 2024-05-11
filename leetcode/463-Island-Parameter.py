# Difficulty : Easy
# Tag : Array, DFS, BFS, Matrix

def islandPerimeter(self, grid: List[List[int]]) -> int:
    res = 0
    # visited = set()

    def checkNeighbour(i,j):
        connIsland = 0
        # north
        if j-1>=0 and grid[i][j-1]==1:
            connIsland+=1
        # east
        if i+1<len(grid) and grid[i+1][j]==1:
            connIsland+=1
        # south
        if j+1<len(grid[0]) and grid[i][j+1]==1:
            connIsland+=1
        # west
        if i-1>=0 and grid[i-1][j]==1:
            connIsland+=1
        
        return connIsland

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                # visited((i,j))
                con = checkNeighbour(i,j)
                res += (4-con)

    return res

        