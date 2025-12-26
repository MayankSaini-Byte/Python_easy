import random 

MAX_LINES=3
MIN_LINES=1
Max_BET=100
Min_BET=1

row=3
columns=3
symbol_dict={
    "A":2,
    "B":4,
    "C":6,
    "D":8

}

symbol_VALUE={
    "A":5,
    "B":4,
    "C":3,
    "D":2

}

def cheak_winning(columns,lines,bet,valuue):
    winning=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winning+=valuue[symbol]*bet
            winning_lines.append(line+1)
    return winning,winning_lines

def get_slot_machine__spin(row,columns,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    col=[]
    for c in range(columns):
        coll=[]
        current_symbols=all_symbols[:]
        for r in range(row):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            coll.append(value)
        col.append(coll)
    return col

def print_Jackpot_machine(col):
    for row in range(len(col[0])):
        for i,column in enumerate(col):
            if i!=len(col)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()
def get_number_of_lines():
        while True:
            try:
                lines=input(f"Enter the no. of lines (Max-{MAX_LINES}and Min-{MIN_LINES}): ")
                if lines.isdigit():
                    lines=int(lines)
                    if MIN_LINES <= lines <= MAX_LINES:
                        return lines
                    else:
                        print("Please enter a no. of lines in given range.")
                else:
                    print("Please enter a digit")
            except Exception as e:
                print(f"There is an Error occur as {e}")

def amount():
    while True:
        try:
            amount=input("Enter the amount you want to deposite $: ")
            if amount.isdigit():
                amount=int(amount)
                if amount>0:
                    return amount
                else:
                    print("Please enter a valid amount")
            else:
                print("Please enter a digit")
        except Exception as e:
            print(f"There is an Error occur as {e}")

def get_bet():
    while True:
        try:
            amount=input("Enter the amount you want to deposite $: ")
            if amount.isdigit():
                amount=int(amount)
                if Min_BET<=amount<=Max_BET:
                    return amount
                else:
                    print(f"Please enter a valid amount between {Min_BET}$ and {Max_BET}$")
            else:
                print("Please enter a digit")
        except Exception as e:
            print(f"There is an Error occur as {e}")

def spin_(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You donot have enough balance.Your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines}. Total bet is {total_bet}")
    Jackpots=get_slot_machine__spin(row,columns,symbol_dict)
    print("\nSlot Machine:")
    print_Jackpot_machine(Jackpots)
    winn,winn_lines=cheak_winning(Jackpots,lines,bet,symbol_VALUE)
    print(f"You are winning ${winn}.")
    print("You won on lines: ",*winn_lines)
    return winn-total_bet

def main():
    balance=amount()
    while   True:
        print(f"Cureent Balcnce id ${balance}")   
        spin=input("Press enter to spin(q to quit).").lower()
        if spin=="q":
            break
        balance+=spin_(balance)
        print(f"You left withh ${balance}")
main()