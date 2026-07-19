# calculator
def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division (a,b):
    return a/b
try:
    a = float(input("enter a number : "))
    b = float(input("enter a number : "))
    choice = input("enter your choice : 1 add, 2 subtract, 3 multiplication, 4 division")
    if choice == "1":
        print(add(a,b))
    elif choice == "2":
        print(subtract(a,b))
    elif choice == "3":
        print(multiplication(a,b))
    elif choice == "4":
        print(division(a,b))
except:
    print("error")