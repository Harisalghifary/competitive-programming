# Difficuly : Easy
# Tag : Array, Linked List, sorting, binary search, Daily leetcode challenge 30 May 2023
class MyHashSet:

    def __init__(self):
        self.set = []
        return None
        
    def add(self, key: int) -> None:
        if self.contains(key):
            return None
        
        self.set.append(key)
        return None
        
    def remove(self, key: int) -> None:
        if not self.contains(key):
            return None
        self.set.remove(key)
        return None

    def contains(self, key: int) -> bool:
        # sorted array
        # binary search
        if key in self.set : return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)