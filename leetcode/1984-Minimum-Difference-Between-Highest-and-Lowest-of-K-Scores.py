# Difficulty : Easy
# Tag : Array, Sorting, Sliding Window
def minimumDifference(self, nums: List[int], k: int) -> int:
    # sort nums for easy checking
    nums.sort()
    # Define Variable
    left, right = 0,k-1
    minDiff = 1e9
    # iterate over input
    while right<len(nums):
        # expand the window
        # Process the window
        minDiff = min(minDiff, nums[right]-nums[left])
        left+=1
        right+=1
    return minDiff