master_password="IWANTtoseethePASSWORDS"
def add():
    name=input("User_name: ")
    pwd=input("Password: ")
    with open("pass.txt","a") as f:
        f.write(name+"||"+pwd+"\n")
def view():
    mp=input("enter the master password to view: ")
    if master_password==mp:
        with open("pass.txt","r") as f:
            data=f.read()
            print(data)
    else:
        print("Incorrcet password")
ask=input("This is a password manager choose the task to operate:\n1.Add\n2.View\n3.Exit\n:").capitalize()
while True:
    try:
        if ask=="Add":
            add()
            break
        elif ask=='View':
            view()
            break
        elif ask=="Exit":
            break
    except Exception as e:
        print("Somthing went wrong!!! with the error of ",e)
        break