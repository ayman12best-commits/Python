#exam eligibility checker
mc = input("Does the student have a medical cause (y/n) : ")
if mc.lower() == 'n':
    att = int(input("enter the attendance : "))
    if att > 75:
        print("The student is allowed to write the exam")
    else:
        print("The student is not allowed to write the exam")
else:
    print("The student is allowed to write the exam")