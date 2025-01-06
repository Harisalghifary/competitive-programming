# Difficulty : Medium
# Tag : dynamic programming, set, Array
def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    dp = [0] * 366
    travelDays = set(days)
    for i in range(366):
        if i not in travelDays:
            # using prev dp
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[max(0,i-1)] + costs[0], 
            (dp[max(0,i-7)] + costs[1]),
            dp[max(0,i-30)] + costs[2])
    
    return dp[365]