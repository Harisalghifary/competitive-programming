import sys
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # define variable
    left, right = 1, max(piles)
    # binary search
    while left<=right:
        # calculate mid
        mid = left + (right-left)//2
        totalHour=0
        # check for totalHour
        for pile in piles:
            totalHour+=(pile+mid-1)//mid
        if totalHour<=h:
            right=mid-1
        else:
            left=mid+1
    return left