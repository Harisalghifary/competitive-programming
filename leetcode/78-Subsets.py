# Difficulty : Medium
# Tag : array, backtracking, bit manipulation
def subsets(self, nums: List[int]) -> List[List[int]]:
    def dfs(idx, curr):
        res.append(curr[:])

        for i in range(idx, len(nums)):
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()

        return res
    res = []
    return dfs(0,[])
    
    # def dfs(idx, curr, used):
    #     if idx==len(nums):
    #         return

    #     for i in range(idx, len(nums)):
    #         curr.append(nums[i])
    #         if tuple(curr[:]) not in used:
    #             res.append(curr[:])
    #             used.add(tuple(curr[:]))
    #         dfs(i+1,curr,used)
    #         curr.pop()
    #     return res

    # res = [[]]
    # dfs(0,[],set())
    # return res