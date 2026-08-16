# class vehicle 
class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage


modelX = vehicle(240,18)
print("The maxspeed of the object is : ",modelX.maxspeed)
print("The mileage of the object is : ",modelX.mileage)