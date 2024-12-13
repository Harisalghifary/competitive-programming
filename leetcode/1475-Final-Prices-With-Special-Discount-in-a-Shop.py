# Difficulty : Easy
# Tag : Array, stack monotonic
def finalPrices(self, prices: List[int]) -> List[int]:
    # check the right
    res = []
    for i in range(len(prices)):
        res.append(prices[i])
        for j in range(i+1,len(prices)):
            if prices[j] <= prices[i]:
                res[i] = (prices[i]-prices[j])
                break

    return res