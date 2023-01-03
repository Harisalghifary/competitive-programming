def minRemoveToMakeValid(self, s: str) -> str:
    result = ""
    s = list(s)
    len_s = len(s)

    count = 0
    for idx, item in enumerate(s):
        if item==")" :
            if count > 0 :
                count-=1
            else:
                s[idx] = '#'

        elif item=="(":
            count+=1

    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i]==")":
            count+=1
        elif s[i]=="(":
            if count > 0:
                count-=1
            else:
                s[i]= '#'
    
    for char in s:
        if char!='#':
            result+=char
    
    return result   