# A simple program to manage a collection of bitcoin purses.
# Each purse has an address and a balance.
purses = {}
import uuid

def generate_address():
    # Generate a random bitcoin address
    return str(uuid.uuid4())

# Add a new purse to the collection
def add_purse():
    address = generate_address()
    balance = 0
    # Don't need to check if address is already in purses because
    # uuid4() generates a unique random address
    purses[address] = balance
    print(f'New purse created with address {address}')

# TODO: Show all the purses in the collection
# For each purse, print the address and the balance
def show_purses():
    # for address, balance in purses.items():
    #     print(f'{address} {balance}')
    for address in purses:
        print(f'{address} {purses[address]} bitcoins')

# TODO: Withdraw bitcoins from a purse
# - check if the address is in the collection
# - check if the purse has enough bitcoins
# - if so, subtract the amount from the purse's balance
# - return true if the withdrawal was successful else false
def withdraw(address, amount):
    if address not in purses:
        print('Address not found')
        return False
    if amount > purses[address]:    # check if amount is greater than balance
        print('Insufficient funds')
        return False
    purses[address] -= amount       # update balance, subtract amount
    return True

# TODO: Deposit bitcoins into a purse
# - check if the address is in the collection
# - if so, add the amount to the purse's balance
# - return true if the deposit was successful else false
def deposit(address, amount):
    if address not in purses:
        print('Address not found')
        return False
    purses[address] += amount    # update balance, add amount
    return True

# TODO: Transfer bitcoins from one purse to another
# - check if the addresses are in the collection
# - check if the source purse has enough bitcoins
# - if so, subtract the amount from the source purse's balance using withdraw()
# - add the amount to the destination purse's balance using deposit()
# - return true if the transfer was successful else false
def transfer(source, destination, amount):
    if source not in purses or destination not in purses:
        print('Either source or destination not found')
        return False
    if amount > purses[source]:    # check if amount is greater than balance
        print('Insufficient funds to transfer')
        return False
    withdraw(source, amount)       # update balance, subtract amount
    deposit(destination, amount)   # update balance, add amount
    print(f'{amount} bitcoins transferred from {source} to {destination}')
    return True
# TODO: Check the balance of a purse
# - check if the address is in the collection
# - if so, print the purse's balance
# - else print an error message
def check_balance(address):
    if address not in purses:
        print('Address not found')
    print(f'{address}: {purses[address]} bitcoins')

def print_menu():
    print('1. Add a new purse')
    print('2. Show all purses')
    print('3. Withdraw bitcoins')
    print('4. Deposit bitcoins')
    print('5. Transfer bitcoins')
    print('6. Check balance')
    print('7. Quit')


def do_task(choice):
    if choice == 1:
        add_purse()
    elif choice == 2:
        show_purses()
    elif choice == 3:
        address = input('Enter address: ')
        amount = int(input('Enter amount: '))
        if withdraw(address, amount):
            print('Withdrawal successful')
        else:
            print('Withdrawal failed')
    elif choice == 4:
        address = input('Enter address: ')
        amount = int(input('Enter amount: '))
        if deposit(address, amount):
            print('Deposit successful')
        else:
            print('Deposit failed')
    elif choice == 5:
        source = input('Enter source address: ')
        destination = input('Enter destination address: ')
        amount = int(input('Enter amount: '))
        if transfer(source, destination, amount):
            print('Transfer successful')
        else:
            print('Transfer failed')
    elif choice == 6:
        address = input('Enter address: ')
        check_balance(address)
    elif choice == 7:
        print('Goodbye')
    else:
        print('Invalid choice')


### Main program ###
EXIT = 7
running = True
while running:
    print_menu()
    choice = int(input("Enter your choice: "))
    do_task(choice)
    running = choice != EXIT