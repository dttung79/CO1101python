import imp


import random as rd
playing = True


while playing:
    number = rd.randint(1, 10)
    guess_number = int(input("Guess a number between 1 and 10: "))
    if number == guess_number:
        print('Correct!')
    else:
        print('Not correct. The number was', number)
    
    playing = input('Do you want to play again? (y/n) ').lower() == 'y'