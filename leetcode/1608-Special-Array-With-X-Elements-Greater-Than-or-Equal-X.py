# Difficulty : Easy
# Tag : Sorring, binary search
def specialArray(self, nums: List[int]) -> int:
    # sort the nums for greedy
    nums.sort()
    res = idx = 0
    total = len(nums)
    # loop through nums
    while idx < total and res<=nums[-1]:
        # change index to next nums
        if res>nums[idx]:
            idx+=1
        # check for curr idx is correct answer
        if res <= nums[idx]:
            # if res == exact count num
            if res == (total-idx):
                return res
            # increment number of x
            res+=1

    return -1