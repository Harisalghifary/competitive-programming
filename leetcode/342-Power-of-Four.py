# Difficulty : Easy
# Tag : Math, Bit Manipulation, Recursion
def isPowerOfFour(self, n: int) -> bool:
    # base condition
    if n==0:
        return False
    # hypothesis
    return n==1 or (n%4==0 and self.isPowerOfFour(n//4))