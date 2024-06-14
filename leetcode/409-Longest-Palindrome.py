from collections import Counter
def longestPalindrome(self, s: str) -> int:
    # if len(s)==1:
    #     return 1
    # flag = False
    # data = Counter(s)
    # count=0

    # for item in data:
    #     if len(data)==1:
    #         return data[item]
    #     if not flag and data[item]%2!=0:
    #         flag = True
    #         count+=data[item]
    #         continue
    #     if (data[item])%2!=0:
    #         count+=data[item]-1
    #         continue
    #     count+=data[item]
    # return count

    res = 0
    isOneOdd = False
    map = Counter(s)

    for key, val in map.items():
        if val>1:
            # handle for odd cases
            # only 1 char with odd count is allowed
            if val%2==1:
                # set to true
                if not isOneOdd:
                    isOneOdd = True
                    res+=val
                else:
                    res+=val-1
            else:
                res+=val
        # handle for char with count = 1
        else:
            # only 1 char with odd count is allowed
            if not isOneOdd:
                res+=val
                isOneOdd = True
    return res