# Difficulty : Easy
# Tag : Math, Dynamic Programming, Recursion, Memoization
def fib(self, n: int) -> int:
    # base condition
    if n<=1:
        return n
    # hypothesis
    return self.fib(n-1) + self.fib(n-2)