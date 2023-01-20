# Difficulty : Easy
# Tag : Array, Two Pointers
def removeDuplicates(self, nums: List[int]) -> int:
    # num_dict = {}
    # idx=0
    # while idx<len(nums):
    #     if nums[idx] in num_dict:
    #         nums.pop(idx)
    #         continue
    #     num_dict[nums[idx]]=1
    #     idx+=1
    # return len(nums)
    # checker = [set(nums)]
    counter = 0
    length = len(nums)
    for i in range(1, length):
        if nums[counter] != nums[i]:
            counter += 1
            nums[counter] = nums[i]
    return counter + 1