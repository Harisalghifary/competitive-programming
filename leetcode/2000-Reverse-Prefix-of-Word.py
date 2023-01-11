def reversePrefix(self, word: str, ch: str) -> str:
    anchor, explorer, n = 0,0, len(word)
    word = list(word)
    while explorer<n:
        if word[explorer]==ch:
            while anchor<=explorer:
                word[anchor], word[explorer] = word[explorer], word[anchor]
                anchor+=1
                explorer-=1
            break
        explorer+=1

    return "".join(word)