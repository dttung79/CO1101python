number1 = int(input('First number: '))

number2 = int(input('Second number: '))

operation = input("Operation [+, -, *, /]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2
elif operation == "*":
    combination = number1 * number2
elif operation == "/":
    if number2 == 0:
        combination = 'You can\'t divide by zero'
    else:
        combination = number1 / number2

print(f"Answer: {combination}")

print()
input("Press return to continue ...")
