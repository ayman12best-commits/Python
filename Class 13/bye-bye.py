# nested while loop - exception
flag = True
try:
    while flag:
        n = int(input("enter the number : "))
        while n%2 == 0:
            print("bye")
        print(n,"is an odd number")
        flag = False
except:
    print("error occured")