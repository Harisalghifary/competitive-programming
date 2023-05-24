def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
    # define variable
    heap = []
    result = totalSum = 0
    # zip = make tuple
    pairs = zip(nums1, nums2)
    # sort by element[1]
    nums = sorted(pairs, key=lambda x: -x[1])

    for num in nums:
        num1, num2 = num
        heapq.heappush(heap, num1)
        totalSum+=num1

        # check if len of heap is more than k
        # if true -> remove smallest element
        if len(heap) > k :
            totalSum-=heapq.heappop(heap)
        # calculate if heap length == k
        if len(heap)==k:
            result = max(result, totalSum*num2)

    return result

