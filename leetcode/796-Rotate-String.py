# Difficulty : Easy
# Tag : String, String matching
def rotateString(self, s: str, goal: str) -> bool:
    # logic
    # check until end if left + right = goal

    if len(s) != len(goal):
        return False

    for i in range(len(s)):
        if s[i:]+s[:i]== goal:
            return True

    return False