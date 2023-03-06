# Difficulty : Medium
# Tag : Array, Divide and Conquer, Sorting, Heap, Merge sort
def sortArray(self, nums: List[int]) -> List[int]:
    if len(nums)>1:
        left, right = 0, len(nums)
        if left > right :
            return
        mid = left+ (right-left)//2
        # split to 2 part
        leftHalf = nums[:mid]
        rightHalf = nums[mid:]
        # recursive call until 
        self.sortArray(leftHalf)
        self.sortArray(rightHalf)

        i = j = k = 0
        # sort and merge two part
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i]>rightHalf[j]:
                nums[k]=rightHalf[j]
                j+=1
            else:
                nums[k]=leftHalf[i]
                i+=1
            k+=1
        # handle if any element in leftHalf was left
        while i<len(leftHalf):
            nums[k]=leftHalf[i]
            i+=1
            k+=1
        # handle if any element in rightHalf was left
        while j<len(rightHalf):
            nums[k]=rightHalf[j]
            j+=1
            k+=1

    return nums