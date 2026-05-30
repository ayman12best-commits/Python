# profit or loss
cp = float(input("enter the cost price of the product : "))
sp = float(input("enter the selling price of the product : "))

if cp > sp:
    print(cp-sp,"is the loss")
else:
    print(sp-cp,"is the profit")