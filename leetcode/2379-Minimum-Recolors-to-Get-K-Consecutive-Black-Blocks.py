# Difficulty : Easy
# Tag : String, Sliding Window
def minimumRecolors(self, blocks: str, k: int) -> int:
    # Define Variable
    count, flips, minOperation = 0, 0, 1e9
    left, right = 0, 0
    # Iterate over input
    while right<len(blocks):
        # Expand the window
        if blocks[right] == "W":
            flips+=1
            count+=1
        elif blocks[right]== "B":
            count+=1
        # Stop condition
        if count == k:
            # Process the window
            minOperation = min(minOperation, flips)
            # Contract the window
            if blocks[left]=="W":
                flips-=1
                count-=1
            else:
                count-=1
            left+=1
        right+=1
    return minOperation