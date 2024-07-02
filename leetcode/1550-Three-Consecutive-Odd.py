# Difficulty : Easy
# Tag: Array
def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    # if len(arr)<3:
    #     return False

    # for i in range(len(arr)-2):
    #     if (arr[i]&1==1) and (arr[i+1]&1==1) and (arr[i+2]&1==1):
    #         return True

    # return False
    window = 0
    for i in range(min(3, len(arr))):
        window+= (arr[i]%2)

    if window == 3:
        return True

    for i in range(3, len(arr)):
        window+= (arr[i]%2)
        window-= (arr[i-3]%2)

        if window == 3:
            return True
    return False
    