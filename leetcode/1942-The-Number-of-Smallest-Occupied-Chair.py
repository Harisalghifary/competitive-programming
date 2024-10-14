# Difficulty: Medium
# Tag: Array, sorting
def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    n=len(times)
    order=sorted((range(n)), key =lambda x:times[x][0])
    seat=[-1]*n
    for i in order:
        ar,lv = times[i]
        for s in range(len(seat)):
            if seat[s]==-1 or seat[s]<=ar:
                if i==targetFriend:
                    return s
                seat[s]=lv
                break
    