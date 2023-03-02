# Difficulty : Medium
# Tag : Array, Queue, Recursion, Math
def findTheWinner(self, n: int, k: int) -> int:
    # recursive function for simulate delete
    def simulateWinner(index: int):
        # base condition
        if len(people)<=1:
            return 
        # index-1+k mod people length for handle circular list
        index = (index+k-1)%(len(people))
        people.pop(index)
        return simulateWinner(index)
    # generate list for people
    people = [x for x in range(1,n+1)]
    simulateWinner(0)
    # return the last people in list
    return people.pop()