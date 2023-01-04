from collections import Counter
def minimumRounds(self, tasks: List[int]) -> int:
    cnt = Counter(tasks)
    result = 0
    for i, value in cnt.items():
        if value < 2:
            return -1
        if value>3:
            temp = value//3
            if value%3==0:
                result+= temp
            else:
                result+= temp+1
        else:
            result+= value//2
    return result