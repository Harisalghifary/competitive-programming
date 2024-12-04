# Difficulty : Medium
# Tag: Two pointer
def canMakeSubsequence(self, str1: str, str2: str) -> bool:
    # define two pointer
    i = j = 0

    while i < len(str1) and j < len(str2):
        # condition logic compare
        if str1[i]==str2[j] or (ord(str1[i])-96+1)%26 == (ord(str2[j])-96)%26:
            i+=1
            j+=1
        else:
            i+=1
    
    # result condition
    if j >= len(str2):
        return True
    
    return False