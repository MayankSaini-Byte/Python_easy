with open("file.txt","r") as f:
    READ=f.readlines()
with open("password.txt","r") as p:
    the_password=p.readline().strip()
print("This is a password inputer for a file to show which is encrypted")
print("If you want to see the file content enter the password")
attempt=3
while attempt>0:
    password=input("Enter the password: ")
    try:
        if password==the_password:
            print("You got the correct password\nThis is the File content")
            print(35*"=")
            for line in READ:
                print(line,end="")
            print("\n",35*"=")
            break
        else:
            attempt-=1
            print(f'You got the password wrong make sure you only have {attempt} attempts left')
            ask=input("You want to enter the pass again ?(y/n)").lower()
            
            if ask=="y":
                    continue
            elif ask=="n":
                    
                    print("You choose not to enter\nHave a good day ahed")
                    break
            else:
                print("Invalid Command")
                break
    except:
        print("SOmthing Went wrong!!!")
        break
if attempt==0:
    print("You are out of attemmpt try again later")