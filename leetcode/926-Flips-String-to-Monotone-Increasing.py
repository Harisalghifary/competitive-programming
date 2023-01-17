def minFlipsMonoIncr(self, s: str) -> int:
    zeros, ones = 0, 0
    for char in s:
        if char == '1':
            ones+=1
        elif char == '0':
            zeros+=1
        zeros = min(zeros, ones)
    return zeros