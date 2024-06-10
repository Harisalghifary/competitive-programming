# Difficulty : Medium
# Tag : Array, hash table, prefix sum

def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    remaindersFound = {0: -1}
    currSum = 0
    
    for i in range(len(nums)):
        currSum += nums[i]
        remainder = currSum % k

        if remainder in remaindersFound:
            # check length > 1
            if i - remaindersFound[remainder]>=2:
                return True
        else:
            # store remainder and current index
            remaindersFound[remainder] = i
    
    return False
        