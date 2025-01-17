item_dict={
    "Apple":[2500,50],
    "Banana":[400,5],
    "Mango":[700,20],
    "Orange":[470,40],
    "Papaya":[500,100],
    "Grapes":[1000,10],
    "Watermelon":[400,200],
    "Dragon Fruit":[600,200],
    "Lichee Fruit":[800,7]
    }

def show_dict():
    print(30*"=")
    print("Available Items and Quantity")
    print(30*"=")      
    for x in item_dict:
         print(x,(15-len(x))*" ",
               (6-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(30*"-")
show_dict()

def dec_quant(key,val):
    item_dict[key][0]-=val
def inc_quant(key,val):
    item_dict[key][0]+=val
    
def receive_order():
    print("Order Received")
    while True:
        item=input("Item(type 'x' to stop):")
        if item=="x":
            break
        value=int(input("Quantity:"))
        if item not in item_dict:
            print("New item Found!")
            uprice = float(input("Unit Price:"))
            item_dict[item] = [value,uprice]
            continue
        inc_quant(item,value)
    show_dict()

def process_demand():
    print("Input Demand")
    # demand_list =
    demand_list = []
    while True:
        item=input("Item(type 'x' to stop):")
        if item=="x":
            break
        if item not in item_dict:
            print(f"The item '{item}' is not available!")
            continue
        value=int(input("Quantity:"))
        if value>item_dict[item][0]:
            print(f"Total of {item_dict[item][0]} pcs are available!")
            continue
        dec_quant(item,value)
        demand_list+=[item,value,
                      item_dict[item][1],value*item_dict[item][1]],
         #printing the payment receipt    
    print(40*"=")
    print("** payment Receipt **".center(40))
    print(40*"=")
    print("Item",7*" ","Quant"," ","U.price",2*" ","S.Total")

    print(40*"-")
    tprice = 0
    for x in demand_list:
        tprice+=x[3]
        print(x[0].title(),(11-len(x[0]))*" ",
              (4-len(str(x[1])))*" ",x[1],
              (7-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
              (10-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print(40*"-")
    print("Total Price:"," ",tprice)
    show_dict()

while True:
    print("Choose an option:")
    print("Type '1': To process demand,")
    print("Type '2': To receive order,")
    print("Type '3': To exit the program,")
    choice= input("Choice: ")
    if choice=='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
              break
    else:
        continue












            
