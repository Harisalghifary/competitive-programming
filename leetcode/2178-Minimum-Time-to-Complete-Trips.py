# Difficulty : Medium
# Tag : Array, Binary Search, Daily Code Challenge 7/6/2023
import sys
def minimumTime(self, time: List[int], totalTrips: int) -> int:
    left, right = 1, sys.maxsize
    # iterate toward input until left>=right
    while left<right:
        # calculate mid
        mid = left + (right-left)//2
        total = 0
        # calculate totalTrips
        for i in time:
            total+=mid//i
            # break for efficiency
            if total>=totalTrips:
                break
        if total>=totalTrips:
            right=mid
        else:
            left=mid+1
    return left