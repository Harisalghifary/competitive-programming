def detectCapitalUse(self, word: str) -> bool:
    if len(word)==1:
        return True
    idx = 0
    word_length = len(word)

    if idx==0 and word[idx].isupper():
        if word[idx+1].isupper():
            for char in word:
                if not char.isupper():
                    return False
            return True
        for i in range(1,word_length):
            if not word[i].islower():
                return False
        return True
    
    for char in word:
        if not char.islower():
            return False

    return True


            