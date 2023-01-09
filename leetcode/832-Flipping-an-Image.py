def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    n = len(image)
    left, right = 0, n-1
    # invert image
    for i in range(n):
        while left<right:
            image[i][left], image[i][right] = image[i][right], image[i][left]
            left+=1
            right-=1
        left, right = 0, n-1
    for i in range(n):
        for j in range(n):
            if image[i][j]==1:
                image[i][j] = 0
            else:
                image[i][j] = 1

    return image