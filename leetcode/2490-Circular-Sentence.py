# Difficulty : Easy
# Tag : string
def isCircularSentence(self, sentence: str) -> bool:
    splitWord = sentence.split(" ")

    for i in range(0,len(splitWord)):
        if i==len(splitWord)-1:
            if splitWord[0][0] != splitWord[i][-1]:
                return False
        elif splitWord[i][-1] != splitWord[i+1][0]:
            return False

    return True
    