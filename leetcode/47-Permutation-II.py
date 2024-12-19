# Difficulty : Medium
# Tag: Backtracking, array, hash table
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    def backtrack(maps, res, curr):
        if n == len(curr):
            res.append(curr[:])
            return

        for key,freq in maps.items():
            if freq == 0:continue

            curr.append(key)
            maps[key]-=1
            backtrack(maps, res, curr)
            curr.pop()
            maps[key]+=1
        return res

    mapNum = Counter(nums)
    res = []
    return backtrack(mapNum, res, [])
    # def backtrack(nums, res, curr, used):
    #     if len(nums) == len(curr):
    #         res.append(curr[:])
    #         return 

    #     # generate
    #     for i in range(len(nums)):
    #         if (used[nums[i]] == 0 or (i!=0 and nums[i]==nums[i-1])):continue
    #         # insert
    #         curr.append(nums[i])
    #         used[nums[i]]-=1
    #         backtrack(nums, res, curr, used)
    #         # cleansing
    #         used[nums[i]]+=1
    #         curr.pop()
    #     return res

    # maps = Counter(nums)
    # nums.sort()
    # res = []
    # backtrack(nums, res, [], maps)

    # return res