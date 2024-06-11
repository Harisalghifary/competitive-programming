# Difficulty : Easy
# Tag : Hash table, Counter, Array
def commonChars(self, words: List[str]) -> List[str]:
    # Initialize the counter with the frequency of characters in the first word
    common_counter = Counter(words[0])
    
    # Update the counter with the minimum frequency of characters found in subsequent words
    for word in words[1:]:
        word_counter = Counter(word)
        for char in common_counter:
            common_counter[char] = min(common_counter[char], word_counter[char])
            
    # Collect the characters based on their frequency in the common_counter
    result = []
    for char, freq in common_counter.items():
        result.extend([char] * freq)
    
    return result