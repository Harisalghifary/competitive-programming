# Difficulty : Medium
# Tag: array, backtracking
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def dfs(idx,curr):
        res.append(curr[:])

        for i in range(idx,len(nums)):
            # skip same value, in same recursive level
            if i>idx and nums[i] == nums[i-1]:continue

            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
        return res

    res = []
    nums.sort()
    return dfs(0,[])