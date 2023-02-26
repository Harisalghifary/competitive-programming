# Difficulty : Easy
# Tag : Recursion, Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # base condition
    if head == None or head.next == None:
        return head
    # induction
    # our linked list return start here
    # iterate until head.next is None
    newHead = self.reverseList(head.next)
    # set prev node to next of newHead
    # it's similiar with newHead.next = head
    head.next.next = head
    # handle for circular linked list
    head.next = None
    return newHead