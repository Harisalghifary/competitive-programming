def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1==s2:
        return True
    diff = []
    length = len(s1)

    for i in range(length):
        if s1[i]!=s2[i]:
            diff.append(i)
            if len(diff)>2:
                return False

    if len(diff)!=2:
        return False

    return s1[diff[0]]==s2[diff[1]] and s1[diff[1]]==s2[diff[0]]

# def areAlmostEqual(self, s1: str, s2: str) -> bool:
#     count = 0
#     c1 = Counter(s1)
#     c2 = Counter(s2)
    
#     if c1 != c2:
#         return False
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             count+=1
#         if count>2:
#             return False

#     if count <=2 :
#         return True
#     return False               