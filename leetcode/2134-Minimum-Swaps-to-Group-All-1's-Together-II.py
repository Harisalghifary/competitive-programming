# Difficulty : Medium
# Tag : Array, sliding window
def minSwaps(self, nums: List[int]) -> int:
    # count nums[x] = 1
    # O(1) space complexity > list.count(1)
    totalOnes = sum(x==1 for x in nums)
    # count x==1 in sizeWindow = totalOnes
    countOnesInCurrWindow = sum(x==1 for x in nums[:totalOnes])
    # define variable
    n = len(nums)
    left, right = 0, totalOnes%n
    maxOnesInWindow = countOnesInCurrWindow
    # iterate over input
    while left<n:
        # add 1 if nums[right]==1 and substract 1 if nums[left]==1
        countOnesInCurrWindow+= nums[right] - nums[left]
        # Process the window
        maxOnesInWindow = max(maxOnesInWindow, countOnesInCurrWindow)
        left+=1
        right=(right+1)%n
    # return minSwaps = totalOnes - maxOnesInCurrWindow
    return totalOnes - maxOnesInWindow
