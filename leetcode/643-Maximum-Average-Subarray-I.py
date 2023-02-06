# Difficulty : Easy
# Tag : array, sliding window
def findMaxAverage(self, nums: List[int], k: int) -> float:
    curr = sum(nums[0:k])
    if len(nums)==k:
        return curr/k

    left, right = 0, k
    globalMaxAvg = curr

    while right<len(nums):
        curr = (curr - nums[left] + nums[right])
        globalMaxAvg = max(globalMaxAvg, curr)
        left+=1
        right+=1

    return globalMaxAvg/k