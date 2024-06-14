# Difficulty : Medium
# Tag : string, prefix, sliding window
def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    # get calculation from char1 to char2 with ascii
    def getCost(char1, char2):
        return abs(ord(char1)-ord(char2))
    # init variable
    l, r = 0, 0
    n = len(s)
    ans = 0
    # move until end while cost is eligible
    while r<n:
        maxCost -= getCost(s[r], t[r])
        # move index left until maxCost is eligible
        while l<=r and maxCost<0:
            maxCost += getCost(s[l], t[l])
            l += 1
        # compare curr answer with new calculation
        ans = max(ans, (r-l+1))
        r += 1
    return ans