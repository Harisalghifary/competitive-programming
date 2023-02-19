# Difficulty : Medium
# Tag : Array, Sliding Window
def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    left, right = 0,minutes
    totalSatisfied = 0
    for val, cond in zip(customers, grumpy):
        if cond==0:
            totalSatisfied+=val
        # else : # cond == 1
        #     totalSatisfied-=val
    maxGrumpyInWindow = grumpyInCurrWindow = sum(num for num, cond in zip(customers[:right], grumpy[:right]) if cond)
    
    while right<len(customers):
        if grumpy[right] == 1:
            grumpyInCurrWindow+= customers[right]
        if grumpy[left] == 1:
            grumpyInCurrWindow-= customers[left]
        maxGrumpyInWindow = max(maxGrumpyInWindow, grumpyInCurrWindow)
        left+=1
        right+=1
    return totalSatisfied + maxGrumpyInWindow