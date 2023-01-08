# medium difficulty
# tag : two pointer, sort
def numSubseq(self, nums: List[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    left, right = 0, n-1
    result = 0
    mod = 10**9+7
    while left<=right:
        if nums[left]+nums[right]<=target:
            result+=pow(2, (right-left), mod)
            left+=1
        else:
            right-=1
        
    return result%mod