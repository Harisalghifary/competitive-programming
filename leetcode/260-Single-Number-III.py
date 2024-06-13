# Difficulty : hash table, array, count, bit manipulation
# Tag : Medium

def singleNumber(self, nums: List[int]) -> List[int]:
    # Map method
    # res = []
    # map = defaultdict(int)

    # for num in nums:
    #     map[num] += 1

    # for num in nums:
    #     if map[num]==1:
    #         res.append(num)
    
    # return res

    xor = i = 0
    if len(nums)==2:
        return nums

    for num in nums:
        xor^=num

    bitSet = xor&-xor
    a = b = 0
    for num in nums:
        if num & bitSet == 0:
            a ^= num
        else:
            b ^= num
    # b = xor^a
    return [a,b]