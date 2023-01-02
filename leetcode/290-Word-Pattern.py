def wordPattern(self, pattern: str, s: str) -> bool:
    dict = {}
    words = s.split(" ")

    if len(pattern) != len(words):
        return False

    for idx, item in enumerate(pattern):
        if len(words[idx])>1 and words[idx] in dict:
            if dict[words[idx]] != item:
                return False
        if item in dict:
            if dict[item] != words[idx]:
                return False
        # assign data to dict
        if len(words[idx])>1:
            dict[words[idx]] = item
        dict[item] = words[idx]
        
    return True
