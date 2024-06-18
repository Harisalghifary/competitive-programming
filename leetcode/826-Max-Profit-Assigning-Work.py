# Difficulty: Medium
# Tag : Array, sorting, greedy, binary search, two pointer
def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    # zip and sort in decrease order to greedy method
    pairDiffProfit = sorted(zip(difficulty,profit), key=lambda x:x[1], reverse=True)
    worker.sort(reverse=True)
    maxProfit = 0
    i = 0
    for work in worker:
        # loop based on prev index
        while i<len(pairDiffProfit):
            if work >= pairDiffProfit[i][0]:
                maxProfit+= pairDiffProfit[i][1]
                break
            i+=1

    return maxProfit