def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = {}
    for idx, item in enumerate(nums):
        n = target-item
        if item in result:
            return [result[item],idx]
        result[n]=idx  