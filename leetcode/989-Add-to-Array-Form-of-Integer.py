# Difficulty : Easy
# Tag : Math
def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    carry = 0
    i = len(num)-1
    while k or carry:
        # check if i is more than 0 for num
        if i >= 0:
            carry += num[i]
        # add value from carry, num, and k
        new_val = carry + k % 10
        # get carry and remainder with divmod
        carry, rem = divmod(new_val, 10)
        if i >=0:
            num[i] = rem
        else:
            num.insert(0, rem)
        i-= 1
        k//=10
    return num