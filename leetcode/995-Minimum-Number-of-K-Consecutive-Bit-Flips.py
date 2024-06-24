# Difficulty : Hard
# Tag : Array, bit manipulation, sliding window, greedy
def minKBitFlips(self, nums: List[int], k: int) -> int:
    n = len(nums)
    isFlippedMode = 0
    flips = 0
    flippedArray = [0] * (n+1)

    for i in range(n):
        isFlippedMode ^= flippedArray[i]
        if nums[i] ^ isFlippedMode == 0: # flip if current is 0 after several flip
            if i+k > n : 
                # it's mean out of boand and impossible
                return -1
            flips+=1
            isFlippedMode ^= 1
            # mark start and end index for flipping
            flippedArray[i] = 1
            flippedArray[i+k] = 1

    return flips