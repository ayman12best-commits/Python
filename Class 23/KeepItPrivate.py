class myclass:
    __privatevar = 27

    def __privatemeth(self):
        print("I am inside a private emthod")
    def hello(self):
        self.__privatemeth()
        print("The private variable",self.__privatevar);

obj1 = myclass()
obj1.hello()
#error
#obj1.__privatemeth()