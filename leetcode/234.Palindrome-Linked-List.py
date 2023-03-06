# Difficulty : Easy
# Tag : Linked List, Two Pointers, Stack, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def checkHalf(head, newHead):
        while newHead:
            if head.val != newHead.val:
                return False
            head = head.next
            newHead = newHead.next
        return True

    def reverseHalf(rHead):
        if not rHead or not rHead.next:
            return rHead
        newHead = reverseHalf(rHead.next)
        rHead.next.next = rHead
        rHead.next = None
        return newHead

    # base condition for palindrome linked list
    if not head or not head.next:
        return True
    slow = fast = head
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
    # after get a middle linked list, reverse the last half and check for first half
    newHead = reverseHalf(slow)
    return checkHalf(head, newHead)