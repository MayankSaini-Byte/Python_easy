import random as r

MIN_LENGTH = 5
MAX_LENGTH = 18

obj = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z',
    '!','@','#','$','%','^','&','*','(',')','_','+','=','?','>','<',
    '[',']','}','{','.'
]

def crafting_pass():
    try:
        length = int(input("Enter the desired length (5-18): "))
        if MIN_LENGTH <= length <= MAX_LENGTH:
            pwd = []
            for _ in range(length):
                pwd.append(r.choice(obj))
            return "".join(pwd)
        else:
            print("Length out of allowed range.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def ask():
    opinion = input("Do you want to create a password (y/n): ").lower()
    if opinion == "y":
        return crafting_pass()
    elif opinion == "n":
        print("Thanks for operating")
        return None
    else:
        print("Invalid choice.")

def main():
    print("\n", "="*12, "Random Password Generator", "="*17, "\n")
    password = ask()
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
