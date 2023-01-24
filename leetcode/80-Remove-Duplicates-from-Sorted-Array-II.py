# Difficulty : Medium
# Tag : Array, Two Pointers
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    # check if len <=2 
    if n<=2:
        return n
    # Define variable
    # fast -> fast pointer
    # slow -> slow pointer
    fast, slow = 2, 2
    while fast < n:
        # check for duplicate
        if nums[slow-2] != nums[fast]:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1

    return slow