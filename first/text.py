

class Vehicle:
    def __init__(self,speed,size):
        self.speed=speed
        self.size=size
    def setSpeed(self,speed):
        self.speed=speed
    def speedUp(self,speed):
        self.speed+=speed
    def speedDown(self,speed):
        self.speed-=speed
vel=Vehicle(10,11)
vel.speedUp(10)
print(vel.speed,vel.size)




