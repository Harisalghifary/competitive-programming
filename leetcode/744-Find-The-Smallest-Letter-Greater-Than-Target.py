# Difficulty : Easy
# Tag : array, binary search, daily leetcode challenge 9 June 2023
def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    # define the ordinary number of target
    asciiTarget = ord(target)

    for letter in letters:
        # checking condition
        if ord(letter) > asciiTarget:
            return letter

    return letters[0]