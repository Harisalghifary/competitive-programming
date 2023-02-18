# Difficulty : Medium
# Tag : Array, Sliding window, hash table
def minimumCardPickup(self, cards: List[int]) -> int:
    # Define variable
    n = len(cards)
    # Check edge case when cards has unique values
    if len(set(cards))==n:
        return -1
    dictCard = defaultdict(int)
    left, right = 0, 0
    minPick = 1e9
    # iterate over input
    while right<n:
        # expand the window
        x = cards[right]
        if x not in dictCard:
            dictCard[x] = right
        # stop condition
        elif x in dictCard:
            # process the current window
            minPick = min(minPick, right-dictCard[x]+1)
            dictCard[x] = right
        left+=1
        right+=1
    return minPick