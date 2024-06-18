# Difficulty : Hard
# Tag : array, greedy
def minPatches(self, nums, n):
    ans = 0
    currVal = 1
    length = len(nums)
    i = 0
    while currVal <= n:
        if i<length and nums[i] <= currVal:
            currVal+=nums[i]
            i+=1
        else:
            currVal+=currVal
            ans+=1
    return ans