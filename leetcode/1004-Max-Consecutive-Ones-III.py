# Difficulty : Medium
# Tag : Sliding window, binary search, prefix sum
def longestOnes(self, nums: List[int], k: int) -> int:
    # Define Variable
    left, right = 0, 0
    countOfZero = 0
    globalMaxResult = 0
    # iterate over input
    while right<len(nums):
        # expand the window
        if nums[right]==0:
            countOfZero+=1
        while countOfZero>k:
            # proccess the window
            globalMaxResult = max(globalMaxResult, right-left)
            # contract the window
            if nums[left]==0:
                countOfZero-=1
            left+=1
        right+=1

    if countOfZero<=k:
        globalMaxResult = max(globalMaxResult, right-left)
    
    return globalMaxResult