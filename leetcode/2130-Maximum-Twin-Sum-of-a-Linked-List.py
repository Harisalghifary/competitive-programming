# Difficulty : Medium
# Tag : Linked List, Two Pointer, Stack, Daily leetcode challenge 17 may 2023
def pairSum(self, head: Optional[ListNode]) -> int:
    def reverseRightHalf(half):
        # this code should reverse linked list reverse right half
        # if not half or not half.next :
        #     return half

        # newHead = reverseRightHalf(half.next)
        # half.next.next = half
        # half.next = None
        # return newHead
        prev = None
        curr = half

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev

    slow = fast = head
    maxSum = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    newHalf = reverseRightHalf(slow)
    # disconnect the half
    slow.next = None

    while head and newHalf:
        maxSum = max(maxSum, head.val+newHalf.val)
        head = head.next
        newHalf = newHalf.next

    return maxSum