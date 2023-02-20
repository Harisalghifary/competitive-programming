# Difficulty : Easy
# Tag : Array, Binary Search
def searchInsert(self, nums: List[int], target: int) -> int:
    # Define variable
    left, right = 0,len(nums)-1
    # iterate over input
    while left<=right:
        # calculate mid index
        mid = (right+left)//2
        # check if value of mid == target
        if nums[mid]==target:
            return mid
        # target in right side
        elif target>nums[mid]:
            left=mid+1
        # target in left side
        else:
            right=mid-1
    # return left if target is not in nums
    return left