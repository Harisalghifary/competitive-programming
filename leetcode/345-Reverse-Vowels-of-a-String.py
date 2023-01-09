def reverseVowels(self, s: str) -> str:
        vowel = ['a','A','i','I','u','U','e','E','o','O']
        left, right = 0, len(s)-1
        s = list(s)
        while left<right:
            if s[left] in vowel and s[right] in vowel:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            elif s[left] in vowel:
                right-=1
            elif s[right] in vowel:
                left+=1
            else:
                left+=1
                right-=1
        
        return "".join(s)