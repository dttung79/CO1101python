PEPSI_PRICE = 1.5
ORANGE_PRICE = 2.0
WATER_PRICE = 0.5
PEPSI_CHOICE = 1
ORANGE_CHOICE = 2
WATER_CHOICE = 3

def print_drinks():
    print('Drinks Menu')
    print(f'{PEPSI_CHOICE}. Pepsi (${PEPSI_PRICE})')
    print(f'{ORANGE_CHOICE}. Orange (${ORANGE_PRICE})')
    print(f'{WATER_CHOICE}. Water (${WATER_PRICE})')

def get_choice():
    # ask user to enter a choice, validate and return a valid choice
    choice = int(input('Your choice: '))
    return choice

def get_ndrinks():
    # ask user to enter number of drinks (1-5), validate and return a valid number
    ndrinks = int(input('Number of drinks: '))
    return ndrinks

def cal_payment(choice, ndrinks):
    # calculate and return payment
    if choice == PEPSI_CHOICE:
        payment = PEPSI_PRICE * ndrinks
    elif choice == ORANGE_CHOICE:
        payment = ORANGE_PRICE * ndrinks
    elif choice == WATER_CHOICE:
        payment = WATER_PRICE * ndrinks
    else:
        return 0
    
    return payment

def pay(payment):
    # ask user to enter amount of money, calculate and print the change
    print(f'You need to pay ${payment}')
    amount = int(input('Insert money: '))
    change = amount - payment
    if change > 0:
        print(f'Your change: ${change}')


#### main program ####
print_drinks()
choice = get_choice()
ndrinks = get_ndrinks()
payment = cal_payment(choice, ndrinks)
pay(payment)