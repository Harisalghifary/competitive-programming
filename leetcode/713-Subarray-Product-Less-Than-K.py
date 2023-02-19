# difficulty : Medium
# tag : array, sliding window
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    # handle edge case
    if k <= 1:
        return 0        
    # define variable
    productSum, countSubArray = 1, 0
    left, right = 0, 0
    while right<len(nums):
        # expand the window
        productSum*=nums[right]
        # stop condition
        while productSum >= k:
            # contract the window
            productSum/=nums[left]
            left+=1
        # process the window
        countSubArray += right-left+1
        right+=1
    return countSubArray
            