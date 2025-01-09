# Difficulty : Easy
# Tag: string, array, hash table
def stringMatching(self, words: List[str]) -> List[str]:
    maps = Counter(words)
    res = []
    for anchor, val in maps.items():
        for word in words:
            if anchor in word and anchor != word:
                res.append(anchor)
                break

    return res