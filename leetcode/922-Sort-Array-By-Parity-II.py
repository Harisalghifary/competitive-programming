def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    left, right, n = 0, 1, len(nums)

    while right<n and left<n:
        if nums[left] % 2 != 0 and nums[right]%2!=1:
            nums[left], nums[right] = nums[right], nums[left]
            left+=2
            right+=2
        elif nums[left]%2==0:
            left+=2
        elif nums[right]%2==1:
            right+=2

    return nums
    