# Difficulty : Easy
# Tag : Array, Sorting, Daily Leetcode Challenge 1 May 2023
def average(self, salary: List[int]) -> float:
    # salary.sort()
    # result = 0
    # for i in range(1, len(salary)-1):
    #     result+=salary[i]

    # return result/(len(salary)-2)
    maxSal = max(salary)
    minSal = min(salary)
    total = sum(salary) - maxSal - minSal
    return total/(len(salary)-2)