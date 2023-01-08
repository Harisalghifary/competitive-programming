import math
def judgeSquareSum(self, c: int) -> bool:
    left, right = 0, int(math.sqrt(c))

    if right*right == c:
        return True
    else:
        left=1
        while left<=right:
            if left**2 + right**2 == c:
                return True
            elif left**2 + right**2 > c:
                right-=1
            else:
                left+=1

    return False