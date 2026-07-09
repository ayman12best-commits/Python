# multiple exception
try:
    n1,n2 = eval(input("enter two number seperated by commas : "))
    r = n1/n2
    print(r)
except SyntaxError:
    print("the value had to be seperated by commas")
except ZeroDivisionError:
    print("The number is divided by zero wrong input")
except:
    ("we need another number")
else:
    print("no exception")
finally:
    print("I will always be there - The program ends")