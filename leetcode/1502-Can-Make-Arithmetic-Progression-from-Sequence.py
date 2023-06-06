# Difficulty : Very Easy
# Tag : Array, Sorting, Daily leetcode challenge 6 June 2023
def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    rasio = arr[1] - arr[0]

    for i in range(1,len(arr)):
        if arr[i]-arr[i-1] != rasio:
            return False

    return True