# Difficulty : Medium
# Tag : Prefix, array, hash table

def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    res = []
    setDict = set(dictionary)
    # split the sentence
    words = sentence.split()

    # loop through word sentence
    for word in words:
        # loop from 0 to len(word)
        for i in range(len(word)+1):
            prefix = word[:i]
            if prefix in setDict:
                res.append(prefix)
                break
        else:
            # handle if not in dict
            res.append(word)

    return " ".join(res)