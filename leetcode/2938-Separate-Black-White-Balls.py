# Difficulty : Medium
# Tag: Twopointer, array
def minimumSteps(self, s: str) -> int:
    left, right = 0, len(s)-1
    swap = 0
    # iterate with two pointer
    # condition
    # if left 0 -> next left + 1
    # elif left 1 -> 
        # if right == 1 -> right - 1
    # swap condition: left = 1 and right = 0
    while left<right:
        print(left,right)
        if s[left] == "0":
            left+=1
        elif s[right] == "1":
            right-=1
        elif s[left] == "1" and s[right] == "0":
            # swap
            swap+= (right-left)
            left+=1
            right-=1
    
    return swap
            

    