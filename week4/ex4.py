s = 0
# Ask user to enter a number. 
n = int(input('Enter a number: '))
while n > 0:
    s = s + n
    n = int(input('Enter a number: '))

# print s
print('Sum of entered positive numbers is', s)