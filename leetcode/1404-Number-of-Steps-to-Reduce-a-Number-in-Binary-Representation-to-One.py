# Difficulty : Medium
# Tag: Bit manipulation
def numSteps(self, s: str) -> int:
    # init variable
    steps = carry = 0
    n = len(s) - 1

    # loop from end to start
    for i in range(n, 0, -1):
        # odd case
        if int(s[i]) + carry == 1:
            carry = 1
            # rules from question
            steps += 2
        # even case
        else:
            steps += 1
    # hande carry in first binary
    return steps + carry