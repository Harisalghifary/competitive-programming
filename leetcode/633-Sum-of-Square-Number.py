# Difficulty : Medium
# Tag : Array, two pointer, binary search
def judgeSquareSum(self, c: int) -> bool:
    a = 0
    b = math.floor(sqrt(c))
    # looping until a>b
    while a<=b:
        # calculate current sum
        currSum = (a*a) + (b*b)
        # handle for valid number
        if currSum == c:
            return True
        # decrease right index
        if currSum > c:
            b-=1
        # increase left index
        elif currSum < c:
            a+=1
    return False