menu = {
      
       "pasta":50,
       "pizza":100,
       "coffee":130,
       "malt cake":100,
       "mix chat":120,
}

print("welcome to python restourent")
print("pasta:RS50\npizza:RS100\ncoffee:RS130\nmalt cake:RS100\nmix chat:RS120 ")

order_total=0

item_1 = input("enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"your item {item_1} has added in your order")

else:
    print(f"order item {item_1} is not available yet")

anothoer_order = input("do you want to another item? (yes/no) ")
if anothoer_order == "yes":
    item2 = input("Enter the name of second item=")
    if item2 in menu:
        order_total += menu[item2]
        print(f"item {item2} has been added to order")
    else:
        print(f"order item {item2} is not availab")

print(f"The total amount of item to pay is  is {order_total}")
    