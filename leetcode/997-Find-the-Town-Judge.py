# Difficulty : Easy
# Tag : Daily Challenge 23 January 2023, Array, Hashmap
def findJudge(self, n: int, trust: List[List[int]]) -> int:
    # Define hashmap for store trust relation each people
    trustsRelation = defaultdict(int)

    # Calculate trustRelation of each people
    for a,b in trust:
        trustsRelation[a] -= 1
        trustsRelation[b] += 1
    
    for i in range(1,n+1):
    # The One who has value of trustRelation == n-1 is the judge
        if trustsRelation[i] == n-1:
            return i
    # Return  -1 if none one of them is judge
    return -1