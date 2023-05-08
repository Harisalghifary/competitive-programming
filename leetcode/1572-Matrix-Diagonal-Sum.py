# Difficulty : Easy
# Tag : array, matrix
def diagonalSum(self, mat: List[List[int]]) -> int:
    n = len(mat)
    primarySum = secondarySum = 0

    for i in range(n):
        for j in range(n):
            if i==j :
                primarySum+=mat[i][j]
            elif i+j == n-1:
                secondarySum+=mat[i][j]

    return primarySum+secondarySum