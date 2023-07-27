# Difficulty : Medium
# Tag : Math, Recursion
def solve(self, x, n):
    # init answer
    ans = 1
    while n > 0:
        # check if even or odd
        # if odd update answer
        if n&1:
            ans *= x
        x *= x
        # shifting == n div 2
        n >>= 1
    return ans

def myPow(self, x: float, n: int) -> float:
    # return early for x == 1
    if x == 1:
        return 1
    
    long_n = abs(n)
    result = self.solve(x, long_n)

    # check for negative
    if n < 0:
        result = 1 / result
    return result