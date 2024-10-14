# Difficulty : Medium
# Tag: heap, sorting
def minGroups(self, intervals: List[List[int]]) -> int:
    heap = []
    intervals.sort(key=lambda x:x[0])

    for start,end in intervals:
        if heap and start>heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap,end)
        
    return len(heap)