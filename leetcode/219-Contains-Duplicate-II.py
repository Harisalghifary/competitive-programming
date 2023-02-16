# Difficulty : Easy
# Tag : Hash table, sliding window
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    dictUniq = defaultdict(int)
    left, right = 0, 0
    count = 0
    while right<len(nums):
        x = nums[right]
        if x not in dictUniq:
            dictUniq[x] = right
        elif x in nums:
            if abs(dictUniq[x]-right)<=k:
                return True
            dictUniq[x] = right
            left+=1
        right+=1
    return False