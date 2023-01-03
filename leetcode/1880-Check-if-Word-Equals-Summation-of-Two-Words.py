def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
    def helper(s: str)->int:
        res = ""
        for char in s:
            res+=str((ord(char)-97))
        return int(res)
    
    return (helper(firstWord)+helper(secondWord))==helper(targetWord)