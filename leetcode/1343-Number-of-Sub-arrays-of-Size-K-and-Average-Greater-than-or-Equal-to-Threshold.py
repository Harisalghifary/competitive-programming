# Difficulty : Medium
# Tag : array, sliding window
def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    left, right = 0, k
    countResult=0
    curr = sum(arr[left:right])
    if curr/k >= threshold:
        countResult+=1
    # iterate for input
    while right<len(arr):
        # calculate with sliding window technique
        curr += arr[right] - arr[left]
        # Contract window
        if curr/k >= threshold:
            countResult+=1
        left+=1
        right+=1
    return countResult