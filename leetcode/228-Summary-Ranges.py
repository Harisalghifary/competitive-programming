# Difficulty : Easy
# Tag : array, daily leetcode challenge 12 June 2023
def summaryRanges(self, nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    result = []
    start = nums[0]

    for i in range(1, len(nums)):
    # check if num with num prev differentiate is more than one
        if nums[i] != nums[i-1] + 1:
            if start == nums[i-1]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[i-1]))
            start = nums[i]
    
    # handle last num
    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(str(start)+"->"+str(nums[-1]))

    return result


            