# Denomination calculator
m = int(input("enter the maths marks : "))
e = int(input("enter the english marks : "))
s = int(input("enter the science marks : "))
h = int(input("enter the hindi marks : "))

sum = m+s+e+h

percentage = sum/400*100
print("The percentage is : ",percentage)