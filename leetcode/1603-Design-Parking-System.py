class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.curr = [0,0,0]
        
    def addCar(self, carType: int) -> bool:
        if carType == 1 :
            if self.curr[0] >= self.big:
                return False
            self.curr[0]+=1
            return True
        if carType == 2 :
            if self.curr[1] >= self.medium:
                return False
            self.curr[1]+=1
            return True
        if carType == 3:
            if self.curr[2] >= self.small:
                return False
            self.curr[2]+=1
            return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)