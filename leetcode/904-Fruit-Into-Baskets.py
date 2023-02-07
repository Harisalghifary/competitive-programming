# Difficulty : Medium
# Tag : Daily Challenge 2/7/23, Array, Sliding window
def totalFruit(self, fruits: List[int]) -> int:
    left, right = 0, 0
    globalMaxPick = 0
    dictBasket = defaultdict(int)
    # iterate for input
    while right<len(fruits):
        # expand the window
        dictBasket[fruits[right]]+=1
        # stop expand condition
        # when length dict >2 
        while len(dictBasket)>2:
            dictBasket[fruits[left]]-=1
            # contract the window
            if dictBasket[fruits[left]]==0:
                dictBasket.pop(fruits[left])
            left+=1
        # Process the window
        globalMaxPick = max(globalMaxPick, right-left+1)
        right+=1

    return globalMaxPick