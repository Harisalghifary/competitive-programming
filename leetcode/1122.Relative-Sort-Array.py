# Difficulty : Easy
# Tag: hash table, sort, array
def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    # counter the arr1 and sort
    arrCounter = Counter(arr1)
    arr1.sort()
    
    setArr2=set(arr2)
    res = []
    for num in arr2:
        if num in arrCounter:
            res.extend([num]*arrCounter[num])

    for num in arr1:
        if num not in setArr2:
            res.append(num)

    return res
