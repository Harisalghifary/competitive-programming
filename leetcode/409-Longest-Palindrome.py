from collections import Counter
def longestPalindrome(self, s: str) -> int:
    if len(s)==1:
        return 1
    flag = False
    data = Counter(s)
    count=0

    for item in data:
        if len(data)==1:
            return data[item]
        if not flag and data[item]%2!=0:
            flag = True
            count+=data[item]
            continue
        if (data[item])%2!=0:
            count+=data[item]-1
            continue
        count+=data[item]
    return count