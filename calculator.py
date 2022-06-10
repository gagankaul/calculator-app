#Python Calculator App

cal_summary = []

def addition(a, b):
    equation = str(a) + " + " + str(b) + " = " + str(a+b)
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(a+b))
    ops_list.append(equation)

def subtraction(a, b):
    print("The difference of "+ str(a) + " and " + str(b) + " is " + str(a-b))
    equation = str(a) + " - " + str(b) + " = " + str(a-b)
    ops_list.append(equation)

def multiplication(a, b):
    print("The product of "+ str(a) + " and " + str(b) + " is " + str(a*b))
    equation = str(a) + " * " + str(b) + " = " + str(a*b)
    ops_list.append(equation)

def division(a,b):
    if b != 0:
        print("The quotient of "+ str(a) + " and " + str(b) + " is " + str(a/b))
        equation = str(a) + " / " + str(b) + " = " + str(a/b)
        return equation
    else:
        print("You cannot divide by zero.")
        equation = "DIV ERROR"
        ops_list.append(equation)

def exponentiation(a, b):
    print("The exponent of "+ str(a) + " and " + str(b) + " is " + str(a**b))
    equation = str(a) + " ** " + str(b) + " = " + str(a**b)
    ops_list.append(equation)

def program_state(all_ops):
    choice = input("Would you like to run the program again (y/n): ")
    if choice != "y":
        print("Calculation Summary: ")
        for each in all_ops:
            print(each)
        print("\nThank you for using the Python Calculator App. Have a nice day!")
        running = False
    else:
        running = True
    return running


#Display welcome message
print("Welcome to the Python Calculator App")

ops_list = []
running = True
while running:
    #Get user input
    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter a number: "))
    operation = input("Enter an operation (addition, subtraction, multiplication, division or exponentiation): ").lower().strip()

    #Calculator loop
    if operation == "addition" or operation == "a":
        addition(num1, num2)
    elif operation =="subtraction" or operation == "s":
        subtraction(num1, num2)
    elif operation == "multiplication" or operation == "m":
        multiplication(num1, num2)
        
    elif operation == "division" or operation == "d":
        division(num1, num2)
        
    elif operation == "exponentiation" or operation == "e":
        exponentiation(num1, num2)
    else:
        print("This is not a valid operation. Try again.")

    running = program_state(ops_list)

    





