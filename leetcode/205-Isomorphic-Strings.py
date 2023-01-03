def isIsomorphic(self, s: str, t: str) -> bool:
    length = len(s)
    if length == 1:
        return True
    dict_s, dict_t = {}, {}
    
    for i in range(length):
        if s[i] in dict_s:
            if dict_s[s[i]]!=t[i]:
                return False
        elif t[i] in dict_t:
            if dict_t[t[i]]!=s[i]:
                return False

        dict_s[s[i]] = t[i]
        dict_t[t[i]] = s[i]
    return True