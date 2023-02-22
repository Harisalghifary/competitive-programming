# Difficulty : Medium
# Tag : Binary Search, Daily code challenge 22/2/2023
def shipWithinDays(self, weights: List[int], days: int) -> int:
    # check if shipment is less or more than days
    # days = maximum time shipment
    def shipLoad(capacity: int) -> bool:
        currDay, currLoad = 1, 0
        for val in weights:
            currLoad+=val
            if currLoad > capacity:
                currDay+=1
                currLoad = val
        return currDay<=days
    # define variable
    totalWeight, maxWeight = 0, -1
    # set left to maxWeight and right to totalWeight
    for weight in weights:
        totalWeight+=weight
        maxWeight = max(maxWeight,weight)
    left, right = maxWeight, totalWeight
    # iterate over input
    while left<right:
        # calculate mid
        mid = left + (right-left)//2
        # check shipment
        # if shipLoad == True -> reduce right, otherwise add left to mid+1
        if shipLoad(mid):
            right = mid
        else:
            left = mid+1
    # return left as least capacity
    return left