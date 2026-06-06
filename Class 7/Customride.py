#Customise your ride
choice = int(input("Enter your choice 1(Bike) 2(Car) : "))
if choice == 1:
    choice1 = (input("Enter your choice A(Yamaha) B(Bullet) : "))
    if choice1 == "A":
        print("You have selected Yamaha for your ride")
    elif choice1 == "B":
        print("You have selected Bullet for your ride")
    else:
        print("Invalid choice")
elif choice == 2:
    choice1 = (input("Enter your choice A(BMW) B(Mercedes) : "))
    if choice1 == "A":
        print("You have selected BMW for your ride")
    elif choice1 == "B":
        print("You have selected Mercedes for your ride")
    else:
        print("Invalid choice")
else:
    print("Invalid")