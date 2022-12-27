    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def createCombo(current, left, right):
            if left==0 and right==0:
                return result.append(current)  
            if left>0:
                createCombo(current+'(', left-1,right)
            if left<right:
                createCombo(current+')', left, right-1)

        createCombo("(",n-1, n)
        return result