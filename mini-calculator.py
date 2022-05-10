print("Welcome to the mini calcuator! Numbers are processed in the same order they are input. For example a - b, a / b, and so on. Please input your numbers accordingly.")
userMenuInput = "n"
while userMenuInput != "q" and userMenuInput != "Q":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter + to add, - to subtract, * to multiply, or / to divide: ")
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        elif num1 != 0:
            print("cannot divide num1 by num2 due to division by zero error. Num2 divide by num 1 is: ")
            print(num2 / num1)
        else:
            print("cannot divide by zero!!")
    else:
         print("Invalid operation input. Try again next time")
    userMenuInput = input("Press q to quit or any key to use again: ")

print("Thanks for using the mini calculator")
        
    
