def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # bruteforce
    # for i in range(len(numbers)):
    #     for j in range(i+1, len(numbers)):
    #         if numbers[i]+numbers[j]>target:
    #             break
    #         if numbers[i]+numbers[j]==target:
    #             return [i+1,j+1]
    # return [-1]
    
    # two pointer
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
    
    # hashmap
    # dict = {}
    
    # for idx, num in enumerate(numbers):
    #     if target-num in dict:
    #         return [dict[target-num]+1,idx+1]
        
    #     dict[num]=idx