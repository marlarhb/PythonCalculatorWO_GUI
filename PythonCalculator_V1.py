operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = None
    print(f"'{operator}' is not a valid operator")

if result is not None:
    print(f"Result: {round(result, 3)}")
