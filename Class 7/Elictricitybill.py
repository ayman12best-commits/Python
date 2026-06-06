#calculate elictricity bill
amt = int(input("Enter the amount : "))
if amt < 50:
    c = amt*2.60+25
elif amt < 100:
    c = amt*3.25+35
elif amt < 200:
    c = amt*5.26+45
else:
    c = amt*7.20+75
print("The electricity amount is : ",c)