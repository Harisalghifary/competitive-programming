# Difficulty : Easy
# Tag : Array, Math
def arraySign(self, nums: List[int]) -> int:
    # define variable
    totalProduct = 1
    # calculate product of nums
    for num in nums:
        totalProduct *= num
    sign = (totalProduct>0) - (totalProduct<0)
    return sign if totalProduct!=0 else 0