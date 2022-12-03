# Ex1: Ask user to enter a positive number until correct input is entered.
# Normal way
number = 0
while number <= 0:
    number = int(input('Enter a positive number: '))
    if number <= 0:
        print('Number must be positive! Try again')
print(number)

# Better way
valid_input = False
while not valid_input:
    number = int(input('Enter a positive number: '))
    valid_input = number > 0
    if not valid_input:
        print('Number must be positive! Try again')