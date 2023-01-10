# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if q is None and p is None:
        return True
    
    elif q is None and p is not None:
        return False
    elif q is not None and p is None:
        return False
    
    
    return ((self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)) and (q.val==p.val))