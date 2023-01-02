def largestOddNumber(self, num: str) -> str:
    idx = len(num)-1
    result = ""
    flag = False
    while idx >= 0 :
        if int(num[idx])%2!=0 and not flag:
            result = num[idx]+result
            flag = True
            idx-=1
            continue
        if flag:
            return (num[:idx+1]+result)
        idx-=1
    return result