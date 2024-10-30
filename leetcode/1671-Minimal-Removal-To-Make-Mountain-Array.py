# Difficulty : Hard
# Tag : Array, dynamic programming, binary search
def minimumMountainRemovals(self, nums: List[int]) -> int:
    def longestInc():
        dp = [0] * len(nums)
        lis = []
        for i in range(len(nums)):
            pos = bisect.bisect_left(lis, nums[i])
            if pos == len(lis):
                lis.append(nums[i])
            else:
                lis[pos]=nums[i]
            dp[i] = pos+1
        
        return dp

    def longestDec():
        dp = [0] * len(nums)
        lds = []
        for i in range(len(nums)-1, -1, -1):
            pos = bisect.bisect_left(lds, nums[i])
            if pos == len(lds):
                lds.append(nums[i])
            else:
                lds[pos]=nums[i]
            dp[i] = pos+1
        return dp
    
    dpInc = longestInc()
    dpDec = longestDec()
    res = 0
    n = len(nums)
    # peak cannot first and last index
    for i in range(1,n-1):
        left = dpInc[i]
        right = dpDec[i]
        if left >1 and right>1:
            res = max(res, left+right-1)
    
    return n-res
