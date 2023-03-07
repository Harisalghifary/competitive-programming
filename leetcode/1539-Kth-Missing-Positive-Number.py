# Difficulty : Easy
# Tag : Array, Binary Search, Daily code challenge 6/3/2023
def findKthPositive(self, arr: List[int], k: int) -> int:
    lastVal = arr[-1]
    setArr = set(arr)
    missVal = []
    for i in range(1,lastVal+1):
        # check missing val in arr
        if i not in setArr:
            missVal.append(i)
    if len(missVal)>=k:
        return missVal[k-1]        
    n = len(missVal)
    return lastVal+k-n

