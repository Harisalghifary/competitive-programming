def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    length, count = len(gas), 0

    left = 0
    right = 0
    remaining = 0

    while (right < len(gas)):
        remaining += (gas[right] - cost[right])
        if (remaining < 0):
            left = right + 1
            right = left
            remaining = 0
        else:
            right += 1
    return left
