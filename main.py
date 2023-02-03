loop = 1            # Value to start infinite loop
innerLoop = 1           # Value to start temporary loop

while loop == 1:            # Start of script loop

    print("Input username to proceed or end to end the program")
    name = input("Username : ")  # Ask Username of user

    if name == "end" or name == "End":
        loop = 0

        print("Ending program...")
    else:
        innerLoop = 1           # Value to start temporary loop

        print("Hello", name)            # Reply to username
        print("What do you need help with?")
        print("For a list of commands input 'list' or '?'")

        while innerLoop == 1:           # Start of command script loop

            cmd = input("Input : ")         # Ask for command input

            # Checks if cmd is the same as one of below commands
            # If true it executes the command
            # If false it requests a new command input

            if cmd == "list" or cmd == "?":         # If cmd = list or ? print a list of usable commands

                print("Command list")
                print(" - ?")
                print(" - add")
                print(" - divide")
                print(" - end")
                print(" - list")
                print(" - multiply")
                print(" - subtract")

            elif cmd == "add":            # Addition

                print("Adding two numbers together...")

                x = int(input("Input first number : "))
                y = int(input("Input second number : "))

                print(x, "+", y, "=", x + y)

            elif cmd == "subtract":           # Subtraction

                print("Subtracting two numbers...")

                x = int(input("Input first number : "))
                y = int(input("Input second number : "))

                print(x, "-", y, "=", x - y)

            elif cmd == "multiply":           # Multiplication

                print("Multiplying two numbers...")

                x = int(input("Input first number : "))
                y = int(input("Input second number : "))

                print(x, "*", y, "=", x * y)

            elif cmd == "divide":         # Division

                print("Dividing two numbers...")

                x = int(input("Input first number : "))
                y = int(input("Input second number : "))

                print(x, "/", y, "=", x / y)

            elif cmd == "end":            # Sets innerLoop value to 0

                print("Goodbye", name)          # Goodbye message

                innerLoop = 0

                # Thereby ending the loop and returning to the main loop

            elif cmd == "balls":

                print("heh balls...")

            elif cmd == "hi" or cmd == "hello":

                print("Hello", name)
                print("How can I help?")

            else:

                print("ERROR: - Command (", cmd, ") could not be found!")
