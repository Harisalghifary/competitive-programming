def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    # concate version
    
    # length1, length2 = len(word1), len(word2)
    # res1, res2 = "", ""

    # for i in range(length1):
    #     res1+=word1[i]
    # for i in range(length2):
    #     res2+=word2[i]
    
    # return res1==res2

    # short version
    return "".join(word1) == "".join(word2)