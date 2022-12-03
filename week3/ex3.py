# TODO: enter number n
# check if n is positive or negative

n = int(input("Enter a number: "))
if n > 0:
    print('{} is positive'.format(n))
elif n < 0:
    print('{} is negative'.format(n))
else:
    print('{} is zero'.format(n))