# stock inventory management
item = ['pencil','eraser','sharpner','notebook','glue']
stock = [12,0,3,7,8]

inventory = {item : stock for item,stock in zip(item,stock)}
print("inventory",inventory)

item_in_stock = [items for items in item if inventory[items] > 0]
print("Item in stock")
print(item_in_stock)

choose_item = input("enter the item to buy")

if choose_item not in item_in_stock or inventory[choose_item] == 0:
    exit()

prices = [10,2,5,20,7]
mprice = int(input("enter the marked up price"))

marked_up_price = [p+mprice for p in prices]
print("the marked up price",marked_up_price)

item_index = item.index(choose_item)
choosen_item_price = marked_up_price[item_index]

print("the price of ",choose_item, "is",choosen_item_price)
inventory[choose_item] = inventory[choose_item]-1

print("******************")
print("item bought",choose_item)
print("item price after marked up",choosen_item_price)
print("Inventory ",inventory)
print("****************************************")