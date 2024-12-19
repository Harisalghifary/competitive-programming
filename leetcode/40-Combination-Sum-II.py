# Difficulty : Medium
# Tag: array, backtracking
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def dfs(idx, curr, target):
        if target == 0 :
            res.append(curr[:])
            return

        for i in range(idx, len(candidates)):
            if i>idx and candidates[i]==candidates[i-1]:continue

            val = candidates[i]
            if target-val >= 0:
                curr.append(val)
                dfs(i+1,curr, target-val)
                curr.pop()
        return res

    res = []
    candidates.sort()
    return dfs(0, [], target)