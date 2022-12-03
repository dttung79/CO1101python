n = int(input('Enter number n (n >= 2): '))
if n < 2:
    print('Are you stupid?')
    exit()
    
i = 2
n_divisors = 0

while i < n:
    if n % i == 0:
        n_divisors += 1
    i += 1

print(f'Number of divisors of {n} is {n_divisors}')