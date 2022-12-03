n = int(input('Enter number n: '))
digit_count = 0
m = n

while n > 0:
    digit_count += 1
    n = n // 10
    
print(f'{m} has {digit_count} digits')