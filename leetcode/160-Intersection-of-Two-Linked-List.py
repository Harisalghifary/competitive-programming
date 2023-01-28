# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Difficulty: Easy
# Tag : Linked List, Two Pointers
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    fast=headA
    slow=headB
    while fast!=slow:
        if fast is None:
            # change to headB
            fast = headB
        else:
            fast = fast.next
        if slow is None:
            # change to headA
            slow = headA
        else:
            slow = slow.next
    return fast