# Difficulty : Medium
# Tag: Sorting, monotonic stack
def maxWidthRamp(self, nums: List[int]) -> int:
    n = len(nums)
    maxWidth = 0
    minIndex = float('inf')

    sortedIndices = sorted(range(n), key=lambda x:nums[x])
    # print(sortedIndices)
    for i in sortedIndices:
        maxWidth = max(maxWidth, i-minIndex)
        minIndex = min(minIndex, i)
    return maxWidth