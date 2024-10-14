# Difficulty : Medium
# Tag: counting, two pointer, stack, greedy
def minSwaps(self, s: str) -> int:
    imbalance = 0
    maxImbalance = 0

    for ch in s:
        if ch == ']':
            imbalance +=1
        else:
            imbalance -=1
        # check each step
        maxImbalance = max(maxImbalance, imbalance)

    # ceiling
    return (maxImbalance+1)//2
    