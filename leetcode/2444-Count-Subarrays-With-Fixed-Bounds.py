# Difficulty : Hard
# Tag : Array, sliding window, queue
def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    # Define variable
    # index of minK and maxK
    minIndex, maxIndex = -1, -1
    startIndexSubArray = 0
    countResult = 0
    # iterate over input
    for i, value in enumerate(nums):
        # stop condition
        if (value<minK or value>maxK):
            # contract the window -> change index of starting sub array
            # change the startIndex when meet bad index
            startIndexSubArray=i+1
            minIndex= -1
            maxIndex= -1
        # expand the window
        if nums[i]==minK:
            minIndex = i
        if nums[i]==maxK:
            maxIndex = i
        # process the window
        if minIndex != -1 and maxIndex != -1:
            countResult+= max(0,min(maxIndex,minIndex)-startIndexSubArray+1)
    return countResult