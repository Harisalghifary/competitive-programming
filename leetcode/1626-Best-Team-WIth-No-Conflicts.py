def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    dp = [0]*(1+max(ages))
    # Sorting based on player scores
    player = sorted(zip(scores, ages))
    for score, age in player:                                       
        dp[age] = score + max(dp[:age+1])
    return max(dp)
