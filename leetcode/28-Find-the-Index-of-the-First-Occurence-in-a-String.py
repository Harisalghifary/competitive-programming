# Difficulty : Medium
# Tag : String, Two Pointer, Daily Code Challenge 3/3/2023
def strStr(self, haystack: str, needle: str) -> int:
    # Define variable
    # A == len(haystack)
    # B == len(needle)
    A, B = len(haystack), len(needle)
    # edge case when A <= B
    # compare A and B size
    if A <= B:
        if (haystack == needle):
            return 0
        else:
            return -1
    # if A > B -> iterate with size B
    # otherwise -> iterate with size A
    # using two pointers
    left, right = 0, B
    while right<=A:
        if haystack[left:right] == needle:
            return left
        left+=1
        right+=1
    return -1
