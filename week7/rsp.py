ROCK = 1
PAPER = 2
SCISSORS = 3
BET = 10

def enter_balance():
    invalid_balance = True
    while invalid_balance:
        balance = int(input('Enter your initial balance: '))
        invalid_balance = balance < 10 or balance > 100
        if invalid_balance:
            print('Invalid balance. Please enter a balance between $10 and $100')
    return balance

import random as rd   
def random_rsp():
    n = rd.randint(1, 4)
    if n == ROCK:
        return 'rock'
    elif n == PAPER:
        return 'paper'
    else:
        return 'scissors'

def get_rsp():
    invalid_choice = True
    while invalid_choice:
        choice = input('Enter your choice (rock, paper, scissors): ').lower()
        invalid_choice = choice != 'rock' and choice != 'paper' and choice != 'scissors'
        if invalid_choice:
            print('Invalid choice. Please enter rock, paper, or scissors')
    return choice

def compare_result(comp_choice, user_choice):
    if comp_choice == user_choice:
        return 'tie'
    
    if (user_choice == 'rock'     and comp_choice == 'scissors') or \
       (user_choice == 'paper'    and comp_choice == 'rock')     or \
       (user_choice == 'scissors' and comp_choice == 'paper'):
        return 'win'
    
    return 'lose'

def is_continue():
    choice = input('Do you want to continue (y/n)? ').lower()
    return choice == 'y'

def update_balance(result, balance):
    reward = BET if result == 'win' else -BET if result == 'lose' else 0
    balance += reward
    # Show user's new balance and return it
    print(f'Your new balance is ${balance}')
    return balance
#### MAIN PROGRAM ####
playing = True
balance = enter_balance()
while playing:
    comp_choice = random_rsp()
    user_choice = get_rsp()
    result = compare_result(comp_choice, user_choice)
    print('Result:', result)
    balance = update_balance(result, balance)
    playing = is_continue()