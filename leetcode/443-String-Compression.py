def compress(self, chars: List[str]) -> int:
    def helpers(index:int, number: int):
        number = list(str(number))
        index+=1
        for char in number:
            chars.insert(index,char)
            index+=1
        return

    current, n = 1, len(chars)-1
    if n==0:
        return 1
    for i in range(n,0,-1):
        if chars[i]==chars[i-1]:
            current+=1
            del chars[i]
            if i==1:
                helpers(0,current)
                current = 1
        else:
            if current>1:
                helpers(i,current)
                current = 1
    return len(chars)