# Difficulty : Medium
# Tag : Array, Stack, Daily Leetcode Challenge 13 April 2023

def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    poppedIndex = 0
    stacked = []
    for val in pushed:
        stacked.append(val)
        # checked if stack.len > 0 and stacked[-1]==popped[i]
        while len(stacked)>0 and stacked[-1]==popped[poppedIndex]:
            stacked.pop()
            poppedIndex+=1
    
    return True if len(stacked)==0 else False
		
        