import re
def isPalindrome(self, s: str) -> bool:
    # remove unused characters
    s = re.sub("[\W_]", "", s).lower()
    first_pointer, second_pointer = 0, len(s)-1
    
    while first_pointer<=second_pointer:
        if s[first_pointer]!=s[second_pointer]:
            return False
        first_pointer+=1
        second_pointer-=1
    
    return True