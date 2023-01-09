def removeElement(self, nums: List[int], val: int) -> int:
    count, index = 0, 0
    while index<len(nums):
        if nums[index]!=val:
            nums[count]=nums[index]
            count+=1
        index+=1
    return count