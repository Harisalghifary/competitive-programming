# Difficulty : Medium
# Tag : Array, Prefix sum
def waysToSplitArray(self, nums: List[int]) -> int:
    total = right = sum(nums)
    left = res = 0

    for i in range(len(nums)-1):
        left+=nums[i]
        right-=nums[i]
        if left>=right:
            res+=1
        
    return res