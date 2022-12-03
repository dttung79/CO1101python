even_count = 0
n = int(input('Enter number: '))

while n > 0:
    if n % 2 == 0:
        even_count = even_count + 1
    n = int(input('Enter number: '))

print('Number of even numbers:', even_count)