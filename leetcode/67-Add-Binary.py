# Difficulty : Easy
# Tag : Bit manipulation, string, math, daily leetcode challenge 14/2/23
def addBinary(self, a: str, b: str) -> str:
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    carry, result = 0, []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        if carry % 2 == 1:
            result.append('1')
        else:
            result.append('0')
        carry = carry // 2
    if carry == 1:
        result.append('1')
    result.reverse()
    return ''.join(result)