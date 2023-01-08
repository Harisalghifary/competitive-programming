# easy difficulty
# tag = two pointer, greedy
def minPairSum(self, nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    left, right = 0, n-1
    total_numbers = []
    while left<right:
        total_numbers.append(nums[left]+nums[right])
        left+=1
        right-=1

    return max(total_numbers)