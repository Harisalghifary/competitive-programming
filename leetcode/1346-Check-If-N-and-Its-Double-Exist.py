# Difficulty : Easy
# Tag : Array, hash table, Two Pointer, Binary Search
def checkIfExist(self, arr: List[int]) -> bool:
    # BF Approach
    # for i in range(len(arr)-1):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] == 2*arr[j] or arr[j] == 2*arr[i]:
    #             return True
    maps = Counter(arr)

    for i in range(len(arr)):
        if arr[i]*2 in maps:
            if arr[i]==0 and maps[arr[i]]<2:
                continue
            # print(arr[i])
            return True
    return False