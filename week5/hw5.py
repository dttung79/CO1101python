
REWARD = 5
LUCKY1 = 4
LUCKY2 = 7

points = 0
playing = True

while playing:
    number = int(input('Enter a number: '))
    if number % LUCKY1 * LUCKY2 == 0:
        points += REWARD
        print(f'{number} is a lucky number! You get {REWARD} points!')
    else:
        print(f'{number} is not a lucky number. You get 0 points.')
        
    playing = input('Do you want to play again? (y/n) ').lower() == 'y'

print(f'You have {points} points.')
