# Difficulty : Medium
# Tag: Backtracking, array
def permute(self, nums: List[int]) -> List[List[int]]:
    def backtrack(nums, res, curr, used):
        # base
        if len(curr) == len(nums):
            res.append(curr[:])
            return
        
        # generate
        for i in range(len(nums)):
            # condition to recursive
            if nums[i] not in used:
                curr.append(nums[i])
                used.add(nums[i])
                backtrack(nums,res, curr, used)
                # backtrack
                val = curr.pop()
                used.remove(val)
        
        return res

    res = []
    backtrack(nums, res, [], set())
    return res