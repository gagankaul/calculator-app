#Python Calculator App

def add(a, b):
    """Add two numbers and return the sum"""
    summation = round(a+b, 4)
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(summation))
    return str(a) + " + " + str(b) + " = " + str(summation)


def subtract(a, b):
    """Subtract two numbers and return the difference"""
    difference = round(a-b, 4)
    print("The difference of "+ str(a) + " and " + str(b) + " is " + str(difference))
    return str(a) + " - " + str(b) + " = " + str(difference)


def multiply(a, b):
    """Multiply two numbers and return the product"""
    product = round(a*b, 4)
    print("The product of "+ str(a) + " and " + str(b) + " is " + str(product))
    return str(a) + " * " + str(b) + " = " + str(product)


def divide(a,b):
    """Divide two numebrs and return the quotient"""
    #Perform division if denominator is not zero
    if b != 0:
        quotient = round(a/b, 4)
        print("The quotient of "+ str(a) + " and " + str(b) + " is " + str(quotient))
        return str(a) + " / " + str(b) + " = " + str(quotient)
    else:
        #Display an error if denominator is zero
        print("You cannot divide by zero.")
        return "DIV ERROR"


def exponent(a, b):
    """Take a number to a power and return the result"""
    power = round(a**b, 4)
    print("The result of "+ str(a) + " raised to the power " + str(b) + " is " + str(power))
    return str(a) + " ** " + str(b) + " = " + str(power)


#Display welcome message
print("Welcome to the Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")

#Initialize an empty list to store all the calculations
history = []
running = True

while running:
    #Get user input
    num1 = float(input("\nEnter a number: "))
    num2 = float(input("Enter a number: "))
    operation = input("Enter an operation ((a)ddition, (s)ubtraction, (m)ultiplication, (d)ivision or (e)xponentiation): ").lower().strip()

    #Calculator loop
    if operation == "addition" or operation == "a":
        value = add(num1, num2)
    elif operation =="subtraction" or operation == "s":
        value = subtract(num1, num2)
    elif operation == "multiplication" or operation == "m":
        value = multiply(num1, num2)
    elif operation == "division" or operation == "d":
        value = divide(num1, num2)
    elif operation == "exponentiation" or operation == "e":
        value = exponent(num1, num2)
    else:
        print("This is not a valid operation. Try again.")
        value = "OPP ERROR"

    history.append(value)

    #Ask user to quit
    choice = input("Would you like to run the program again (y/n): ")
    if choice != "y":
        print("\nCalculation Summary: ")
        for each in history:
            print(each)
        print("\nThank you for using the Python Calculator App. Have a nice day!")
        running = False
