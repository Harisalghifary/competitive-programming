# Difficulty : Medium
# Tag : array, binary search, dailly leetcode challenge 25 July 2023
def peakIndexInMountainArray(self, arr: List[int]) -> int:
    # define variable
    left, right = 0, len(arr)-1
    # iterate until left >= right
    while right>left:
        # calculate mid
        # avoid overflow
        mid = left + (right-left)//2
        if arr[mid]<arr[mid+1]:
            left = mid + 1
        else:
            right = mid

    return left