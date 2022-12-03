number1_str = input(" First number: ")
number1 = int(number1_str)

number2_str = input("Second number: ")
number2 = int(number2_str)

operation = input("Operation [+, -, *, /]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2
elif operation == "*":
    combination = number1 * number2
elif operation == "/":
    combination = number1 / number2
else:
    combination = "ERROR ... '" + operation + "' unrecognised"

print(f"Answer: {combination}")

print()
input("Press return to continue ...")
