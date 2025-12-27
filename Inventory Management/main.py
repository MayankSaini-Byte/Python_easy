FILE_NAME = "data.txt"

def loading_inventory():
    inventory={}
    try:
        with open(FILE_NAME,"r") as file:
            for line in file:
                line=line.strip()
                if line=='':
                    continue
                item_id,name,amm,price=line.split("|")
                inventory[item_id]={
                    "name":name,
                    "quantity":int(amm),
                    "price":float(price)
                }
    except FileNotFoundError:
        open(FILE_NAME, "w").close()
    return inventory
inventory=loading_inventory()


def save_theinventory():
    with open(FILE_NAME,"w") as file:
        for item_id,item in inventory.items():
            line=f'{item_id}|{item['name']}|{item["quantity"]}|{item["price"]}\n'
            file.write(line)



def add_the_item():
    item_id=input("Enter item id: ").strip()    
    name=input("Entr the name of item: ").strip()
    if item_id in inventory:
        print("Item alrready Exist.!!")
        return
    try:
        amount=int(input("Enter the amount: "))
        price=float(input("Enter the price:$ "))
        if amount<0 or price<0:
            print("Invlid value !!!")
            return
    except Exception as e:
        print(f"An error occur which is '{e}'")
        return
    inventory[item_id]={
        "name":name,
        "quantity":amount,
        "price":price}
    
    save_theinventory()
    print("ITEM saved!!!")


def take_out():
    item_id=input("Enter the itwm id:  ")
    if item_id not in inventory:
        print("item not found!!!")
        return
    try:
        qty=int(input("entr the ammount you want to take out: "))
        if qty<0:
            print("invalid ammount!!!")
            return
    except :
        print("error")
        return
    if inventory[item_id]["quantity"]<qty:
        print("Insufficient Stock")
        return
    inventory[item_id]["quantity"]-=qty
    save_theinventory()
    print("Item succesfully taken out")

def view():

    if not  inventory:
        print("Empty inventory!!!")
        return
    print("-"*10,"INVENTORY","-"*10)
    for item_id, item in inventory.items():
        print(f'{item_id}|{item["name"]}|{item['quantity']}|${item["price"]}')
        print('-'*29)

def main():
    while 1==1:
        print("\n=============Inventory management==================")
        print('''1.Add Item\n2.Take out Items\n3.View The inventory\n4.Exit''')
        choice=input("Enter the choice: ").strip()
        if choice=="1":
            add_the_item()
        elif choice=="2":
            take_out()
        elif choice=="3":
            view()
        elif choice=="4":
            print("DATA SAFFELY STORED")
            break

main()