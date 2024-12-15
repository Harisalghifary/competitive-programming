# Difficulty : Easy
# Tag : Heap, array, sort
def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    # loop until k
    # proceed the minimum
    # using heap

    heap = []
    for i, num in enumerate(nums):
        heappush(heap,(num,i))

    # print(heap)
    for _ in range(k):
        curr, idx = heappop(heap)
        curr *= multiplier
        heappush(heap, (curr,idx))

    temp = sorted(heap, key=lambda x:x[1])
    res = []
    for val, _ in temp:
        res.append(val)
    return res