# Demomination calculator

amt = int(input("enter the amount : "))

note100 = amt//100
note50 = (amt%100)//50
note10 = ((amt%100)%50)//10

print("The 100 ruppee note = ",note100)
print("The 50 ruppee note = ",note50)
print("The 10 ruppee note = ",note10)