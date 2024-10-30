# Difficulty : Medium
# Tag : Array, Dynamic Programming, binary search
def lengthOfLIS(self, nums: List[int]) -> int:
    # n = len(nums)
    # # init dp
    # dp = [1] * n

    # for i in range(1,n):
    #     for j in range(i):
    #         if nums[i]>nums[j]:
    #             dp[i] = max(dp[i], dp[j]+1)
    
    # return max(dp)

    # using dp and binser

    dp = [0] * len(nums)
    lis = []

    for i in range(len(nums)):
        pos = bisect.bisect_left(lis, nums[i])

        # if greater
        if pos == len(lis):
            lis.append(nums[i])
        else:
            lis[pos] = nums[i]
        dp[i] = pos+1

    return max(dp)
    



    