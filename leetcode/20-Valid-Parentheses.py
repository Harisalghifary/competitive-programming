def isValid(self, s: str) -> bool:
    stack = ['(', '{', '[']
    s1, i = [], 0
    
    if len(s)%2 != 0:
        return False

    while (i<len(s)):
        if s[i] in stack:
            s1.append(s[i])
            i+=1
            
        elif s1:
            if s[i] == ')' and s1[-1]!='(':
                return False
            if s[i] == '}' and s1[-1]!='{':
                return False
            if s[i] == ']' and s1[-1]!='[':
                return False
            s1.pop()
            i+=1
        else:
            return False
    if len(s1)>0:
        return False
    return True