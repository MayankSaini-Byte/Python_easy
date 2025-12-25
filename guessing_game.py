import random as r
easy=["apple","train","tiger","money","india"]
medium=["python123","monkey098","hihimzedar000","tmkoc12345","123mayank"]
hard=["Elephannt@1","iamtheGREAT000","DancingbIRD1234567890"] 
print("\nWelcome to the Password Guessing Game\n")
print("Choose the Difficulty level\n")
try:
    difficulty=input("easy/medium/hard").lower()
    if difficulty =="easy":
        password=r.choice(easy)
    elif difficulty =="medium":
        password=r.choice(medium)
    elif difficulty =="hard":
        password=r.choice(hard)
except:
    print("Enter a valid level, Defaulting to easy level")
    password=r.choice(easy)

attempt=0
print("\nGuess the password ")
while True:
    user_pass=input("Enter the guess: ")
    attempt+=1
    if user_pass==password:
        print(f'Congratulatio! You guessed it in {attempt} attemots.')
        break
    hint=""
    for i in range(len(password)):
        if i<len(password) and user_pass[i]==password[i]:
            hint+=user_pass[i]
        else:
            hint+="_"
    print("Hint",hint)
print("Game over")