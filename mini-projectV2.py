import json
import csv

# variables
Product_list = [""]
Courier_list = [""]
Orders = [{}]
#WEEK 4 CREATE ORDER STATUS LIST
#populating varibles from external files
with open("products.csv", 'r') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    Product_list.append(row)

with open("couriers.csv", 'r') as file:
  reader = csv.reader(file, delimiter=',')
  for row in reader:
    Courier_list.append(row)

with open("orders.csv", 'r') as file:
  reader = csv.DictReader(file, delimiter=',')
  for row in reader:
    Orders.append(row)

#main menu
print("""
-----------------------------------------------------
          Please pick an option:
        1. product menu
        2. couriers menu
        3. orders menu
        0. Save and Exit
-----------------------------------------------------""")
#menu navigation
Menu_selection = input("Enter")
if(int(Menu_selection) == 0):
#WEEK4 SAVE AND EXIT
    exit
elif (int(Menu_selection) == 1): 
    #products menu
    print("""
-----------------------------------------------------
          Please pick an option:
        1. View all products
        2. Create a product
        3. Update products 
        4. Delete products
        0. Exit
-----------------------------------------------------""")

    Menu_selection = input("Enter menu selection:")

    if (int(Menu_selection) == 0):
            exit
    elif (int(Menu_selection) == 1):                                            #1. create a product
        print(Product_list)
    elif (int(Menu_selection) == 2):                                            #1. view products
        Product_list.append(str(input("Add product:")))             
    elif (int(Menu_selection) == 3):                                            #3. update a product
        for (i, item) in enumerate(Product_list, start=0):
            print(i, item)
        Product_selection = input("Enter product index to update?")
        New_product_name = input("Enter new product name?")
        Product_list[int(Product_selection)] = str(New_product_name)
    elif (int(Menu_selection) == 4):                                             #4. delete a product
        for (i, item) in enumerate(Product_list, start=0):
            print(i, item)
        Product_list.pop(int(input("Enter product index to delete:")))
    else: 
        print("invalid option")
elif (int(Menu_selection) == 2): 
    #couriers menu
    print("""
-----------------------------------------------------
          Please pick an option:
        1. View all couriers
        2. Create a courier
        3. Update couriers 
        4. Delete couriers
        0. Exit
-----------------------------------------------------""")
    Menu_selection = input("Enter menu selection:")

    if (int(Menu_selection) == 0):
            exit
    elif (int(Menu_selection) == 1):                                            #1. create a product
        print(Courier_list)
    elif (int(Menu_selection) == 2):                                            #1. view products
        Courier_list.append(str(input("Add courier:")))             
    elif (int(Menu_selection) == 3):                                            #3. update a product
        for (i, item) in enumerate(Courier_list, start=0):
            print(i, item)
        Courier_selection = input("Enter courier index to update?")
        New_Courier_name = input("Enter new courier name?")
        Courier_list[int(Courier_selection)] = str(New_Courier_name)
    elif (int(Menu_selection) == 4):                                             #4. delete a product
        for (i, item) in enumerate(Courier_list, start=0):
            print(i, item)
        Courier_list.pop(int(input("Enter courier index to delete:")))
    else: 
        print("invalid option")

elif (int(Menu_selection) == 3): 
    #orders menu
    print("""
-----------------------------------------------------
          Please pick an option:

        1. View all orders
        2. New order
        3. Update order status
        4. Update order info
        5. Delete order

-----------------------------------------------------""")
    Menu_selection = input("Enter:")
    if (int(Menu_selection) == 0):
        exit
    elif (int(Menu_selection) == 1):                                            
        print(Orders)
    elif (int(Menu_selection) == 2):                                            
        NewOrder = {
        "customer name": "placeholder",
        "customer address": "placeholder",
        "customer phone number": 0000,
        "order status": "pending"}
        NewOrder["customer name"] = str(input("Enter customer full name:"))
        NewOrder["customer address"] = str(input("Enter customer address:"))
        NewOrder["customer phone number"] = str(input("Enter customer phone number:"))
        NewOrder["order status"] = str(input("Enter customer order status:"))
        Orders.append(NewOrder)
        print("Order saved!")                       
    elif (int(Menu_selection) == 3):
        for item in enumerate(Orders):
            print(item)
        Order_selection = input("Enter order index to update?")
        print("current status of order " + str(Order_selection) + " : " + Orders[int(Order_selection)]["orderStatus"])
        del Orders[int(Order_selection)]['orderStatus']
        Orders[int(Order_selection)]['orderStatus'] = input("update status:") 
    elif (int(Menu_selection) == 4):
        for a in enumerate(Orders):
            print(a)
        selection = input("Enter order index to update?")
        b = Orders[int(selection)]
        for c in b:
            print(b)
            print("current selection is " + c)
            d = input("input new detail:")
            if d == "":
                continue
            else:
                b[c] = d
        print(b)
    elif (int(Menu_selection) == 5):
        for item in enumerate(Orders):
            print(item)
        Orders.pop(int(input("Enter order index to delete?")))
        print(Orders)
    else: 
        print("invalid option")


gfsgsfd

