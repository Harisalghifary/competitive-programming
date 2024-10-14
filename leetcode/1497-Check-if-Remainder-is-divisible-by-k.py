# Difficulty: Medium
# Tag: Counting, array, hash
def canArrange(self, arr: List[int], k: int) -> bool:
    # count remainder
    remainderCount = [0]*k
    for num in arr:
        remainder = num % k

        # handle negative value
        if remainder < 0 :
            remainder += k

        remainderCount[remainder] += 1

    # handle zero remainder
    if remainderCount[0] % 2 != 0:
        return False
    
    for i in range(1,k//2+1):
        if remainderCount[i] != remainderCount[k-i]:
            return False

    return True
