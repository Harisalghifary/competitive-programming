# Difficulty : Easy
# Tag : Math, Bit Manipulation, Recursion
def isPowerOfTwo(self, n: int) -> bool:
    # base condition
    if n==0:
        return False
    # hypothesis
    return (n==1) or (n%2==0 and self.isPowerOfTwo(n//2))