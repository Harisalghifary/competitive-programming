# Difficulty : Medium
# Tag : sliding window, array, hashtable

def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    left, right = 0, k
    maxSub = 0
    curr = sum(nums[left:right])
    freq = {}

    for i in range(left,right):
        freq[nums[i]] = freq.get(nums[i],0)+1

    while right<len(nums):
        if len(freq) == k:
            maxSub = max(maxSub, curr)
        if right >= len(nums):
            break

        curr-= nums[left]
        curr+=nums[right]
        freq[nums[left]] -= 1
        if freq[nums[left]] == 0:
            del freq[nums[left]]
        freq[nums[right]] = freq.get(nums[right],0)+1
        right+=1
        left+=1
    
    if len(freq) == k:
        maxSub = max(maxSub, curr)
    return maxSub
        