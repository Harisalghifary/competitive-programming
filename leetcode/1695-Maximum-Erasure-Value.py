# Difficulty : Medium
# Tag : Hash table, sliding window, two pointer, string, array
def maximumUniqueSubarray(self, nums: List[int]) -> int:
    # Define variable
    uniqDict = {}
    left, right = 0,0
    globalMaxValue, curr = 0, 0
    # iterate over input
    while right<len(nums):
        # expand the window
        x = nums[right]
        uniqDict[x] = uniqDict.get(x,0)+1
        curr+=x
        # stop window expand condition
        while left<right and uniqDict[x]>1:
            # contract the current window
            uniqDict[nums[left]]-=1
            curr-=nums[left]
            left+=1
        # process the current window
        globalMaxValue = max(globalMaxValue, curr)
        right+=1
    return globalMaxValue