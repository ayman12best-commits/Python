# BMI Checker

w = float(input("enter the weight in kgs. : "))
h = float(input("enter the height in m : "))

bmi = w/    (h* h)
print("your BMI is :",bmi)
if bmi < 18.5:
    print("You are under weight")
elif bmi < 25:
    print("You are under healthy")
elif bmi < 35:
    print("You are over weight")
else:
    print("You are obese")