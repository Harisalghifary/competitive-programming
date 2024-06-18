# Difficulty : Medium
# Tag : sliding window, array
def countSubarrays(self, nums: List[int], k: int) -> int:
    # init variable
    currCount = left = right = 0
    res = 0
    # find max number in nums
    maxNum = max(nums)
    n = len(nums)
    # loop until len(nums)
    while right<n:
        # calculate maxNum count
        if nums[right]== maxNum:
            currCount+=1
        # sliding window contract
        while currCount>=k:
            # dec currCount if nums[left] == maxNum
            if nums[left]==maxNum:
                currCount-=1
            # formula logic
            # if [i,j] valid subarray then i..j,j+1,j+2,...,len(nums) is valid
            res+= n-right
            left+=1
        right+=1
    return res