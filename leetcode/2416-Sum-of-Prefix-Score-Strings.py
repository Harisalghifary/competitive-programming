class Trie:
    def __init__(self):
        self.prefixCount = 0
        self.children = {}

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # build trie
        root = Trie()
        
        score = []

        # insert to trie each word
        for word in words:
            current = root
            # iterate each char
            for ch in word:
                if ch not in current.children:
                    current.children[ch] = Trie()
                # update the current
                current = current.children[ch]
                # counting
                current.prefixCount +=1


        # calculate each trie to score
        for word in words:
            current = root
            temp = 0
            for ch in word:
                current = current.children[ch]
                temp += current.prefixCount

            score.append(temp)
        return score
        