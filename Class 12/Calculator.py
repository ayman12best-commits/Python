# calculator
def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b

a = int(input("enter the number 1 : "))
b = int(input("enter the number 2 : "))
ch = input("1. Addition \n2.Subtraction \n3. Multiplication \n4. Division Enter your choice : ")
if ch == "1":
    print("the addition of the of two numbers is ",add(a,b))
elif ch == "2":
    print("the subtraction of the of two numbers is ",sub(a,b))
elif ch == "3":
    print("the multiplication of the of two numbers is ",mul(a,b))
elif ch == "4":
    print("the division of the of two numbers is ",div(a,b))