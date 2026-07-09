# value error
try : 
    n = int(input("enter a number : "))
    print(n)
except ValueError as e:
    print("the error occured",e)
