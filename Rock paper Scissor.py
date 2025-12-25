import random as r
choices=["rock","paper","scissor"]
def get_user_choise():
        while True:
            user_input=str(input("Ok so choose (rock/paper/scissor):")).lower()
            if user_input  in choices:
                    return user_input   
            else:
                   print("invalid")
while True:
    random_choice=r.choice(choices)
    ask=str(input("Don you want to play Rock Paper Scissor(y/n): ")).lower()
    if ask=="y":
            user_input=get_user_choise()
            if user_input==random_choice:
                print(f'its a tie both wee and you chosess {user_input}')
            elif user_input == "scissor":
                if random_choice=="paper":
                    print(f'Hurray!! You won\nPython chosess {random_choice} and you {user_input}')
                elif random_choice=="rock":
                    print(f'OHH!! Python\nPython chosess {random_choice} and you {user_input}')
            elif user_input == "rock":
                if random_choice=="paper":
                    print(f'OHH!  Python\nPython chosess {random_choice} and you {user_input}')
                elif random_choice=="scissor":
                    print(f'Hurray!! you You\nPython chosess {random_choice} and you {user_input}')
            elif user_input == "paper":
                if random_choice=="scissor":
                    print(f'Ohh!! Python\nPython chosess {random_choice} and you {user_input}')
                elif random_choice=="rock":
                    print(f'Hurray!! you You\nPython chosess {random_choice} and you {user_input}')
    elif ask=="n":
                print("Thanks for your time")
                break




 
