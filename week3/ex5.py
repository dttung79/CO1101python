# TODO: Enter day of week in number
# Print out the day of week in name
# Check if input is valid (1-7)

day_of_week = int(input('Enter day of week in number: '))
if day_of_week < 1 or day_of_week > 7:
    print('Invalid input')
elif day_of_week == 1:
    print('Sunday')