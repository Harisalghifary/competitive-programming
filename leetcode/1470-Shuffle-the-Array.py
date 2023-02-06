# Difficulty : Easy
# Tag : Array
def shuffle(self, nums: List[int], n: int) -> List[int]:
    # using two pointer
    result = []
    left = 0
    right = n
    while right<2*n:
        result.append(nums[left])
        result.append(nums[right])
        left+=1
        right+=1
    
    return result
