# Difficulty : Easy
# Tag : Array, Hash table, two pointer
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def checkIntersect(nums):
        temp = []
        for num in nums:
            if num in maps and maps[num]>0:
                temp.append(num)
                maps[num]-=1
        return temp

    res = []
    if len(nums1)>=len(nums2):
        # insert nums2 to map
        maps = Counter(nums2)
        res = checkIntersect(nums1)
    else:
        # insert nums1 to map
        maps = Counter(nums1)
        res = checkIntersect(nums2)

    return res