import art

def add(n1, n2):
    return n1 + n2

#TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

#TODO:Add these functions to a dictionary as values with the keys being the operators

#creating the dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)

    should_continue = True
    first_no = float(input("What is your first number? "))
    while should_continue:
        second_no = float(input("What is your second number? "))
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation from above ")

        answer = operations[operator](first_no,second_no)
        print(f"{first_no} {operator} {second_no} = {answer}")

        keep_calc = input(f"Type y to continue calculating with {answer} or n to start a new calculation ").lower()
        if keep_calc == 'y':
            first_no = answer
        else:
            should_continue = False
            print("\n" * 10)
            calculator()
