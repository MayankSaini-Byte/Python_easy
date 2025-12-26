with open("History.txt", "a+") as h:

    while True:
        task = input("""Enter the task to perform for this history based calc
1.Addition
2.Subtraction
3.Multiplication
4.Division
Or Enter Command like 
"History" to show History
"Clear" to Clear the History
And "Exit" to exit
""").capitalize()

        def addition(eq):
            result = eval(eq)
            h.write(str(result) + "\n")
            return result

        def subtraction(eq):
            result = eval(eq)
            h.write(str(result) + "\n")
            return result

        def multiplication(eq):
            result = eval(eq)
            h.write(str(result) + "\n")
            return result

        def division(eq):
            result = eval(eq)
            h.write(str(result) + "\n")
            return result

        try:
            if task == "Addition":
                eq = input("Enter the eq: ")
                print("Result:", addition(eq))

            elif task == "Subtraction":
                eq = input("Enter the eq: ")
                print("Result:", subtraction(eq))

            elif task == "Multiplication":
                eq = input("Enter the eq: ")
                print("Result:", multiplication(eq))

            elif task == "Division":
                eq = input("Enter the eq: ")
                print("Result:", division(eq))

            elif task == "History":
                h.seek(0)
                print(h.read())

            elif task == "Clear":
                h.truncate(0)
                h.seek(0)
                print("History cleared")

            elif task == "Exit":
                print("Thanks for using our Calc")
                break

            else:
                print("Invalid command")

        except:
            print("Invalid input")
