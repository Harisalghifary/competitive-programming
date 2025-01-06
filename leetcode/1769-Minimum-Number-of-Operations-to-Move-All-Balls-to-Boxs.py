# Difficulty : Medium
# Tag : Array, Prefix Sum, String
def minOperations(self, boxes: str) -> List[int]:
    res = []
    n = len(boxes)

    count = curr = 0
    for i in range(n):
        res.append(count)
        curr += int(boxes[i])
        count += curr

    count = curr = 0
    for i in range(n-1, -1, -1):
        res[i]+=count
        curr += int(boxes[i])
        count += curr
    
    return res

    # prefSum = [0] * len(boxes)

    # # forward
    # for i in range(len(boxes)):
    #     for j in range(i,len(boxes)):
    #         if boxes[j]=="1":
    #             prefSum[i]+=abs(j-i)

    # # backward
    # for i in range(len(boxes)-1,-1,-1):
    #     for j in range(i, -1, -1):
    #         if boxes[j]=="1":
    #             prefSum[i]+=abs(j-i)

    # return prefSum