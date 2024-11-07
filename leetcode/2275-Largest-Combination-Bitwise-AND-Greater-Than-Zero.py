# Difficulty: Medium
# Tag: bit manipulation, hash table, array
def largestCombination(self, candidates: List[int]) -> int:
    maps = {}
    
    def calBits(n):
        i = 0
        while n:
            if n & 1 == 1:
                # insert to map
                if i not in maps:
                    maps[i] = 1
                else:
                    maps[i] +=1
            i+=1
            n>>=1
        return

    for i in range(len(candidates)):
        calBits(candidates[i])
    
    res = 0

    for key, val in maps.items():
        res = max(res, val)

    return res