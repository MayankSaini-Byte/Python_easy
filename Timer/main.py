import time 
from playsound import playsound

CLEAR='\033[2J'
CLEAR_RETURN='\033[H'
def alarm(second):
    try:
        if second <= 0:
            print("Timer must be greater than zero.")
            return
        time_elapse=0
        print(CLEAR)
        while time_elapse<second:

            time.sleep(1)
            time_elapse+=1
            time_left=second-time_elapse
            min_left=time_left//60
            sec_left=time_left%60
            print(f'{CLEAR_RETURN}{min_left:02d}:{sec_left:02d}')
        print()
        playsound("fire_alarm.mp3") 
    except FileNotFoundError:
        print("Audio file not found. Check file name/path.")
    except Exception as e:
        print(f"An error occur which is '{e}'")
def ask():
    try:
        mint=int(input("Enter the min.: "))
        sec=int(input("Enter the sec.: "))
        total_sec=mint*60 +sec
        if mint < 0 or sec < 0:
            raise ValueError("Negative time is not allowed")
        return total_sec
    except ValueError as e:
        print(f"Invalid input: {e}")
        return 0
def ask():
    try:
        mint = int(input("Enter the min.: "))
        sec = int(input("Enter the sec.: "))
        if mint < 0 or sec < 0:
            raise ValueError("Negative time is not allowed")
        return mint * 60 + sec
    except ValueError as e:
        print(f"Invalid input: {e}")
        return 0
def main():
    print("\n","="*30,"TIMER","="*30,"\n")
    try:
        decision=input("Dou you want to set a timer(y/n): ").lower()
        if decision=="y":
            print("You choose to set the time")
            print()
            alarm(ask())
        elif decision=="n":
            print("Thanks for operating")
            return
    except Exception as e:
        print("Please enterr valid term")
        print("An error occur which is '{e}'")

if __name__=="__main__":
    main()