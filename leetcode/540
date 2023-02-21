# Difficulty : Medium
# Tag : Array, Binary Search
def singleNonDuplicate(self, nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    # iterate until left>right
    while left<=right:
        # calculate mid
        # handle overflow with this technique
        mid = left+(right-left)//2
        caseA = mid%2==0 and nums[mid] != nums[mid-1]
        caseB = mid%2!=0 and nums[mid] != nums[mid+1]
        # descision choices
        if caseA or caseB:
            left = mid+1
        else:
            right = mid-1
    return nums[left-1]