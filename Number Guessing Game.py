import random
n=random.randint(1,100)
while True:
    try:
        i=int(input("Enter the number between 1 and 100: "))
        if n>i:
                print("Too Low!")
        if n<i:
                print("Too High!")
        if n==i:
                print("Congratulation! You guessed the number ")
                break
    except ValueError :
        print("Enter a valid number")

