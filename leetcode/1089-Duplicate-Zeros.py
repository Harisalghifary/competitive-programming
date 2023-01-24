# Difficulty : Easy
# Tag : Two Pointers, Array
def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    # count the zeroes occurence
    zeroes = arr.count(0)
    n = len(arr)
    anchor = n-1
    # looping from len(arr) to 0
    while anchor>=0:
        # skip if anchor+zeroes has more than n
        if anchor+zeroes < n:
            arr[anchor+zeroes] = arr[anchor]
        if arr[anchor] == 0:
            # decrease 0 in zeroes by 1
            zeroes-=1
            if anchor+zeroes<n:
                arr[anchor+zeroes] = 0
        anchor-=1
    return
