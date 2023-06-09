# Difficulty : Easy
# Tag : array, binary search, matrix
def countNegatives(self, grid: List[List[int]]) -> int:
    # O(n*m)
    # negatives = 0
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] < 0 :
    #             negatives += 1
    # return negatives

    # O(n+m)
    rows, colls = len(grid), len(grid[0])
    row, col = rows-1, 0
    negatives = 0
    while row>=0 and col<colls:
        if grid[row][col]<0:
            negatives += colls - col
            row -= 1
        else: 
            col += 1

    return negatives