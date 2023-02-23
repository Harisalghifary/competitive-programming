# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # base condition
        if head == None:
            return None
        # induction
        head.next = self.removeElements(head.next,val)
        # hypothesis
        return ( head.next if head.val==val else head)