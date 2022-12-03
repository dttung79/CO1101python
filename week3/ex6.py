import random as rd

name = input('Enter name: ')
number = rd.randint(1, 10)

print(f'Hello {name}, your lucky number is {number}')
if number in (3, 9):
    print('and you won a prize!')
elif number == 7:
    print('and you hit the jackpot!')

shape = input('Enter shape: ')
if shape not in ('square', 'circle', 'triangle'):
    print('Invalid shape')
else:
    