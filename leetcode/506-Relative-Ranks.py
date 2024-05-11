# Difficulty : Easy
# Tag: Array, Sorting, Greedy
def findRelativeRanks(self, score: List[int]) -> List[str]:
    sortedScore = []
    for i in range(len(score)):
        sortedScore.append((i+1, score[i]))

    sortedScore.sort(reverse=True, key =lambda x: x[1])
    # print(sortedScore)
    for i, s in enumerate(sortedScore):
        sortedScore[i]=(s[0],i+1)
    
    sortedScore.sort(key=lambda x:x[0])
    res = []
    for i, s in enumerate(sortedScore):
        if s[1] <= 3:
            if s[1]==1:
                res.append("Gold Medal")
            elif s[1]==2:
                res.append("Silver Medal")
            elif s[1]==3:
                res.append("Bronze Medal")
        else:
            res.append(str(s[1]))

    return res




        

    