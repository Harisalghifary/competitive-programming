# Difficulty : Medium
# Tag : Prefix sum, hash table, array

def subarraysDivByK(self, nums: List[int], k: int) -> int:
    remaindersFound = defaultdict(int)
    remaindersFound[0]=1
    res = currSum = 0

    for i in range(len(nums)):
        currSum+=nums[i]
        remainder = currSum %k
        res += remaindersFound[remainder]
        remaindersFound[remainder]+=1

    return res