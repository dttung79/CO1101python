# Write a program that ask user for names & ages of 2 brothers
# Calculate the age different between 2 brothers and print it out

young_brother_name = input('Enter young brother name: ')
young_brother_age = int(input('Enter young brother age: '))

old_brother_name = input('Enter old brother name: ')
old_brother_age = int(input('Enter old brother age: '))

# calculate the age difference between 2 brothers
age_difference = old_brother_age - young_brother_age
print('The age difference between', young_brother_name, 'and', old_brother_name, 'is', age_difference)