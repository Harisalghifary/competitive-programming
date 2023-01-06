def maxIceCream(self, costs: List[int], coins: int) -> int:
    costs.sort()
    max_result = 0
    for cost in costs:
        if coins < cost :
            break
        max_result+=1
        coins-=cost
    return max_result