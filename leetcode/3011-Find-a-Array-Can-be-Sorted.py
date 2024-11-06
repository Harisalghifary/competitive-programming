# Difficulty : medium
# Tag : sorting, array, bits manipulation
def canSortArray(self, nums: List[int]) -> bool:
    segmentArray = []

    def countBits(n):
        count = 0
        while n:
            count += n&1
            n>>=1
        return count
    
    temp = [nums[0]]
    for i in range(1,len(nums)):
        if countBits(nums[i]) != countBits(nums[i-1]):
            segmentArray.append(temp)
            temp = []

        temp.append(nums[i])
        if i == len(nums)-1:
            segmentArray.append(temp)
    
    # print('s', segmentArray)
    res = []
    for i in range(len(segmentArray)):
        segmentArray[i].sort()
        res.extend(segmentArray[i])
    # print('res', res)
    for i in range(1,len(res)):
        if res[i]<res[i-1]:
            return False

    return True