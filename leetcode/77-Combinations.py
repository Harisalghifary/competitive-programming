# Difficulty : Medium
# Tag : Backtracking
def combine(self, n: int, k: int) -> List[List[int]]:
    def backtrack(res, curr, idx):
        if len(curr)==k:
            res.append(curr[:])

        for i in range(idx,n+1):
            curr.append(i)
            # backtrack
            backtrack(res, curr, i+1)
            curr.pop()

        return res
    
    res = []
    return backtrack(res, [], 1)