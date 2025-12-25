import random as r
subject = [
    "Mahatma Gandhi",
    "Dr. B. R. Ambedkar",
    "Jawaharlal Nehru",
    "Narendra Modi",
    "A. P. J. Abdul Kalam",
    "Sachin Tendulkar",
    "Virat Kohli",
    "Amitabh Bachchan",
    "Ratan Tata",
    "Sundar Pichai"
]
action = [
    "riding a buffalo like a bike",
    "dancing in freezing winter wearing shorts",
    "arguing with a ceiling fan",
    "running from a tiny dog like it’s a lion",
    "celebrating WiFi reconnecting",
    "slipping on a banana peel in slow motion",
    "talking to phone while it’s on mute",
    "trying to open a door that says PUSH",
    "wearing sunglasses at night indoors",
    "shadow boxing with own reflection"
]
places = [
    "middle of a busy highway",
    "on top of a water tank",
    "inside an empty classroom during holidays",
    "under a banyan tree at noon",
    "behind the last bench in class",
    "on a railway platform at 5 a.m.",
    "rooftop during a power cut",
    "outside a closed shop on Sunday",
    "at a tea stall during exam time",
    "in a park when mosquitoes are on duty"
]

def randomsubject():
    s=r.choice(subject)
    return s
def randomaction():
    a=r.choice(action)
    return a
def randomplace():
    p=r.choice(places)
    return p

while True:
    try:
        ask=str(input("Do you want to creat a funny and Fake Headline(y/n): ")).lower()
        if ask=='y':
            print("⚠️ This is a Fake News Headline ⚠️")
            print(f'{randomsubject()} {randomaction()} {randomplace()}.')
        elif ask=="n":
            print("Thanks for playing")
            break
    except :
        print("Invalid Command")