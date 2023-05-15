# Difficulty : Medium
# Tag : Linked List, Two Pointer, Daily leetcode challenge 16 May 2023
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # swap value
    first = second = current = head

    for _ in range(k-1):
        first = first.next

    current = first

    while current.next:
        current = current.next
        second = second.next

    temp = first.val
    first.val = second.val
    second.val = temp

    return head