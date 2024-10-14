# Difficulty : Medium
# Tag: Hash table, sorting
def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if the length is the same
        if len(word1) != len(word2):
            return False
        
        # Create character frequency maps
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Check if both words contain the same characters
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        # Check if the frequency counts match (ignoring the characters)
        return sorted(freq1.values()) == sorted(freq2.values())
