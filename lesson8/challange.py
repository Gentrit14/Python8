def calculate(number1, number2, operator):
    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        return "Error: Invalid number input"


    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"



print(calculate(10, 5, '+'))
print(calculate(10, 5, '/'))
print(calculate(10, 0, '/'))
print(calculate(10, 5, '%'))


user_input1 = input("Enter first number: ")
user_input2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")

result = calculate(user_input1, user_input2, operator)
print("Result: ", result)
