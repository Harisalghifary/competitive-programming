# Difficulty : Medium 
# Tag : Linked List, Stack, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # base condition
    if not head.next:
        return head

    newHead = self.removeNodes(head.next)
    # compare two val
    # change currMax -> head.val
    if head.val >= newHead.val :
        head.next = newHead
        newHead = head
    # remove node from newHead
    else:
        head.next = None

    return newHead