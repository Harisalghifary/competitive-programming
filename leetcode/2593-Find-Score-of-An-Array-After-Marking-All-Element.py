# Difficulty : Medium
# Tag : heap, hash table, sorting, greedy, simulation
def findScore(self, nums: List[int]) -> int:
    n = len(nums)
    ord = list(range(n))
    ord.sort(key=lambda x: (nums[x], x))
    
    mark = [False] * n
    res = 0
    for index in ord:
        if mark[index]==True: continue
        res += nums[index]
        # how to mark adjacent
        if index > 0:
            mark[index-1] = True
        if index < n-1:
            mark[index+1] = True
    
    return res