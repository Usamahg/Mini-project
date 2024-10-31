import json
import csv

# variables
Product_list = [{}]
Courier_list = [{}]
Orders = [{}]
Order_status_list = ['pending','awaiting payment','awaiting shipment','shipped','awaiting pickup','completed','declined','refunded','disputed']

#populating varibles from additional files
with open("products.csv", 'r') as file:
  reader = csv.DictReader(file, delimiter=',')
  for row in reader:
    Product_list.append(row)

with open("couriers.csv", 'r') as file:
  reader = csv.DictReader(file, delimiter=',')
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
    with open("products.csv", mode='w') as csvfile:
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
        writer.writeheader()
        for items in Product_list:
            writer.writerow(items)
    with open("couriers.csv", mode='w') as csvfile:
            fieldnames = ['name','phone number']
            writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
            writer.writeheader()
            for items in Courier_list:
                writer.writerow(items)
    with open("orders.csv", mode='w') as csvfile:
        fieldnames = ["customer name", "customer address", "customer phone number", "order status"]
        writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
        writer.writeheader()
        for items in Orders:
            writer.writerow(items)
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
    elif (int(Menu_selection) == 1):                                           
        print(Product_list)
    elif (int(Menu_selection) == 2):                                           
        New_product = {}
        New_product["name"] = str(input("enter product name"))
        New_product["price"] = int(input("enter product price"))
        Product_list.append(New_product)  
    elif (int(Menu_selection) == 3):                                         
        for (i, item) in enumerate(Product_list, start=0):
            print(i, item)
        Product_selection = int(input("Enter product index to update?"))
        a = str(input("Enter New product name:"))
        if (a != ''):
            del Product_list[int(Product_selection)]['name']
            Product_list[Product_selection]['name'] = a

        aOrder = str(input("Enter New product price:"))
        if (aOrder != ''):
            del Product_list[Product_selection]['price']
            Product_list[Product_selection]['price'] = aOrder
    elif (int(Menu_selection) == 4):                                             
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
    elif (int(Menu_selection) == 2):     
        New_courier = {}
        New_courier["name"]= str(input('Enter courier name:'))
        New_courier["phone number"]= str(input('Enter courier\'s phone number:'))
        Courier_list.append(New_courier)             
    elif (int(Menu_selection) == 3):                                            #3. update a product
        for (i, item) in enumerate(Courier_list, start=0):
            print(i, item)
        Courier_selection = int(input("Enter courier index to update?"))
        New_Courier_name = str(input("Enter new courier name?"))
        if (New_Courier_name != ''):
            del Courier_list[int(Courier_selection)]['name']
            Courier_list[int(Courier_selection)]['name'] = New_Courier_name
        
        New_Courier_number = int(input("Enter new courier number?"))
        if (New_Courier_number != ''):
            del Courier_list[int(Courier_selection)]['phone number']
            Courier_list[int(Courier_selection)]['phone number'] = New_Courier_number
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
        NewOrder = {}
        NewOrder["customer name"] = str(input("Enter customer full name:"))
        NewOrder["customer address"] = str(input("Enter customer address:"))
        NewOrder["customer phone number"] = str(input("Enter customer phone number:"))

        #WEEK4-products:
        for (i, item) in enumerate(Product_list, start=0):
            print(i, item)
        Multiple_index = list(map(int, input("Enter \(multiple\) products index:").split()))
        #WEEK4-couriers:
        for (i, item) in enumerate(Courier_list, start=0):
            print(i, item)
        Courier_index = int(input("Enter courier index to update?"))

        NewOrder["order status"] = str(input("Enter customer order status:"))
        Orders.append(NewOrder)
        print("Order saved!")                       
    elif (int(Menu_selection) == 3):
        for item in enumerate(Orders):
            print(item)
        Order_selection = int(input("Enter order index to update?"))
        # print("current status of order " + str(Order_selection) + " : " + Orders[int(Order_selection)]["orderStatus"])
        # del Orders[int(Order_selection)]['orderStatus']
        # Orders[int(Order_selection)]['orderStatus'] = input("update status:") 
        for item in enumerate(Order_status_list):
            print(item)
        status_selection = int(input("Enter new status index?"))
        Orders[Order_selection]['order satus'] = Order_status_list[status_selection]
    elif (int(Menu_selection) == 4):
        for item in enumerate(Orders):
            print(item)
        selection = int(input("Enter order index to update?"))
        aOrder = Orders[int(selection)]
        for key in aOrder:
            print(aOrder)
            print("current selection is " + key)
            New_product = str(input("input new detail:"))
            if New_product == "":
                continue
            else:
                aOrder[key] = New_product
        print(aOrder)
    elif (int(Menu_selection) == 5):
        for item in enumerate(Orders):
            print(item)
        Orders.pop(int(input("Enter order index to delete?")))
        print(Orders)
    else: 
        print("invalid option")


