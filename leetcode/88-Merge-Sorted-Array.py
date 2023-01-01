def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    idx1, idx2, write_idx = m-1, n-1, m+n-1
    
    while idx2>=0:
        if idx1>=0 and nums1[idx1]>nums2[idx2]:
            nums1[write_idx]=nums1[idx1]
            idx1-=1
        
        else:
            nums1[write_idx]=nums2[idx2]
            idx2-=1
        
        write_idx-=1
                
    return nums1