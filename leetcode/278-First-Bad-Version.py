def firstBadVersion(self, n: int) -> int:
    right = n
    mid = n//2
    left = 1
    if n==1:
        return 1
    while left<right:
        mid = (right+left)//2
        
        if not isBadVersion(mid):
            left = mid+1
        elif isBadVersion(mid):
            right = mid
            
    return right