# Difficulty : Easy
# Tag : Array, Sort, Two Pointers
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m-1
    j = n-1
    k = m+n-1
    # iterate from end
    while j>=0:
        if i>=0 and nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i-=1
            k-=1
        else: 
            # nums1[m] < nums2[n]
            nums1[k] = nums2[j]
            j-=1
            k-=1
    return nums1