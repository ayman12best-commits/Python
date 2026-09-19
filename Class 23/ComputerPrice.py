class computer:
    def __init__(self):
        self.__computerprice = 1000

    def display(self):
        print("The computer price",self.__computerprice)
    def setprice(self,price):
        self.__computerprice=price

comp1 = computer()
comp1.display()
comp1.__computerprice = 2000 # the price will not get updated
comp1.display()
comp1.setprice(4690)
comp1.display()