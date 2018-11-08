# Define a factorial function to use the operation inside the calculator
def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

# Define the calculator function
def simple_calculator():
    import math

    print("Here's what you can do...\n")
    print("1.Addition\n2.Subtraction\n3.Product\n4.Division\n5.Power\n6.Factorial\n7.Log\n8.Square root\n")

    # try/except loop to make sure the user enters the right type of value
    while True:
        try:
            operation = int(input('Which operation do you want to perform (choose the number of the operation)?\n'))
        except ValueError:
            print('Invalid input, enter a Number')
            continue
        else:
            if operation in range(1,9):
                break
            # if the operation doesn't exist
            else:
                print('I don\'t do this operation')
                continue

    # If the operation requires two numbers...
    if operation in range(1,6):
        while True:
            try:
                x = int(input('Give me the first number:\t'))
                y = int(input('Give me the second number:\t'))
            except ValueError:
                print('Invalid input, enter a number\n')
                continue
            else:
                break
    # Otherwise if it requires only one number ...
    else:
        while True:
            try:
                x = int(input('Give me a number:\t'))
            except ValueError:
                print('Invalid input, enter a number\n')
                continue
            else:
                break

    # ADDITION
    if operation == 1:
        result = x + y
        print(f'{x} + {y} = {result}')
    # SUBTRACTION
    elif operation == 2:
        result = x - y
        print('{} - {} = {}'.format(x,y,result))
    # MOLTIPLICATION
    elif operation == 3:
        result = x * y
        print(f'{x} * {y} = {result}')
    # DIVISION
    elif operation == 4:
        result = x / y
        print('{} / {} = {}'.format(x,y,round(result)))
    # POWER
    elif operation == 5:
        result = math.pow(x,y)
        print(f'{x}^{y} = {int(result)}')
    # FACTORIAL
    elif operation == 6:
        result = factorial(x)
        print(f'!{x} = {result}')
    # NATURAL LOG
    elif operation == 7:
        result = math.log(x)
        print(f'ln({x}) = {result}')
    # SQUARE ROOT
    elif operation == 8:
        result = int(math.sqrt(x))
        print(f'Square of {x} = {result}')

# CALLING THE CALCULATOR
simple_calculator()
