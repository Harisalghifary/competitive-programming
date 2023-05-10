# Difficulty : Medium
# Tag : array, matrix, daily leetcode challenge 10 may 2023
def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
          return [[1]]

        # define variable
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1
        result = []
        iterator = 1

        # check until center
        while left<=right and top<=bottom:
            # right direction
            for i in range(left, right+1):
                # result.append(matrix[top][i])
                matrix[top][i] = iterator
                iterator+=1
            top += 1
            
            # down direction
            for i in range(top, bottom+1):
                # result.append(matrix[i][right])
                matrix[i][right] = iterator
                iterator+=1
            right -= 1
            
            # left direction
            if top <= bottom:
                for i in range(right, left-1, -1):
                    # result.append(matrix[bottom][i])
                    matrix[bottom][i] = iterator
                    iterator+=1
                bottom -= 1
            
            # up direction
            if left <= right:
                for i in range(bottom, top-1, -1):
                    # result.append(matrix[i][left])
                    matrix[i][left] = iterator
                    iterator +=1
                left += 1
        
        return matrix