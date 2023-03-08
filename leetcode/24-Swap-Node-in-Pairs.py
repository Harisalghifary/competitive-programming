# Difficulty : Medium
# Tag: Linked List, Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # base case
    if not head:
        return None
    if not head.next:
        return head
    # swap adjacent nodes
    first = head
    second = head.next
    third = second.next
    first.next = self.swapPairs(third)
    second.next = first
    return second
    # return newHead
    # first = 1
    # second = 2
    # something = ()
    # second -> first -> something