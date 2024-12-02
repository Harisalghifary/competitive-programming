# Difficulty : Easy
# Tag : array, string, two pointer, string matching
def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    # split each word
    words = sentence.split(" ")
    n = len(searchWord)
    # check the length
    for i, word in enumerate(words):
        if len(word)>=n:
        # process if len(word) == len(searchword)
            if searchWord == word[:n]:
                return i+1

    return -1