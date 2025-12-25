import random
while True:
    a=str(input("You want to roll a dice(y/n):")).lower()
    if a=="y":
        print(f"({random.randint(1,6)},{random.randint(1,6)})")
    elif a=="n" :
        print("Thanks for playing")
        break
    else:
        print("Invalid Command")