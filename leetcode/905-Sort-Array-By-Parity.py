def sortArrayByParity(self, nums: List[int]) -> List[int]:
    explorer = 0
    anchor = len(nums)-1
    while explorer<=anchor:
        if nums[anchor]%2==0 and nums[explorer]%2==1:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor-=1
            explorer+=1
        elif not nums[anchor]%2==0:
            anchor-=1
        elif nums[explorer]%2==0:
            explorer+=1
    return nums
        