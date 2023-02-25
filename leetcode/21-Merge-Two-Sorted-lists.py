# Difficulty : Easy
# Tag : Linked List, Recursion
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def merge(l1,l2,i):
        # base condition
        # append rest of list to list that ended first
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        # move node that have value lesser than other
        if l1.val<=l2.val:
            l1.next = merge(l1.next, l2,i)
            return l1
        else:
            l2.next = merge(l1,l2.next,i)
            return l2
    return merge(list1,list2,i=0)