import random
computer = random.randint(1,50)
while True:
    n = int(input("Enter your guess : "))
    if n == computer:
        print("You have found the number!")
        break
    elif n > computer:
        print("You have guessed above the number")
    else:
        print("You have guessed under the number")