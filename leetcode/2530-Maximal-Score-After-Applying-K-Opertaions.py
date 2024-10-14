# Difficulty : Medium
# Tag: heap, sorting
def maxKelements(self, nums: List[int], k: int) -> int:
    heap = [-num for num in nums]
    res = 0
    heapq.heapify(heap)

    for _ in range(k):
        top = -heapq.heappop(heap)
        res += top
        top = ceil(top/3)
        heapq.heappush(heap, -top)
    return res