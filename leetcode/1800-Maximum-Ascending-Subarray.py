# Difficulty : easy
# Tag : array
def maxAscendingSum(self, nums: List[int]) -> int:
    n, inc = len(nums), nums[0]
    ans = inc
    if n==1:
        return inc
    for i in range(1,n):
        if nums[i]>nums[i-1]:
            inc += nums[i]
        else:
            inc = nums[i]
        ans = max(ans, inc)

    return ans