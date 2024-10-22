# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        res = []
        while q:
            level = 0
            levelSize = len(q)

            for _ in range(levelSize):
                node = q.popleft()
                level+= node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
        
        # sort the res to find kth
        res.sort()

        if k > len(res):
            return -1
        return res[-k] 

        