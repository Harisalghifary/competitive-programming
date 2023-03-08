# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # merge step
    def reorder(head, newHead):
        while head and newHead:
            nextHead = head.next
            nextNewHead = newHead.next
            head.next = newHead
            newHead.next = nextHead
            head = nextHead
            newHead = nextNewHead
        return head
    # reverse second half
    def reverseHalf(half):
        if not half or not half.next:
            return half
        newHead = reverseHalf(half.next)
        half.next.next = half
        half.next = None
        return newHead
    
    if not head.next:
        return head
    # find middle linkedlist
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    newHead = reverseHalf(slow.next)
    slow.next = None

    return reorder(head,newHead)

         
