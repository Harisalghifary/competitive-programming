def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # # Bruteforce
    # length_nums = len(nums)
    # for i in range(length_nums):
    #     min_index = i
    #     for j in range(i+1, length_nums):
    #         if nums[j]< nums[min_index]:
    #             min_index = j
                
                
    #     nums[min_index], nums[i] = nums[i], nums[min_index]

    # two pointers

    left, mid, right = 0, 0, len(nums)-1
    while mid<=right:
        if nums[mid]==0:
            nums[mid], nums[left] = nums[left], nums[mid]
            mid+=1
            left+=1
        elif nums[mid]==1:
            mid+=1
        elif nums[mid]==2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right-=1

    return nums