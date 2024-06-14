# Difficulty : Medium
# Tag : Array, sorting, greedy
def minIncrementForUnique(self, nums: List[int]) -> int:
    if len(nums)==1:
        return 0
    # sort
    nums.sort()
    increment = 0
    # start from 1 to end
    for i in range(1,len(nums)):
        if nums[i]<=nums[i-1]:
            diff = abs(nums[i]-nums[i-1])+1
            increment+= diff
            nums[i]+= diff

    return increment