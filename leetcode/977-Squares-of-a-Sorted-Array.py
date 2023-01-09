def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left, mid, right = 0, 0, n-1
    while left<right:
        if abs(nums[left])>nums[right]:
            temp = abs(nums[left])
            nums.remove(nums[left])
            nums.insert(right, temp)
        else:
            right-=1

    for i in range(n):
        nums[i] = nums[i]*nums[i]
    return nums