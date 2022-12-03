# Enter grade and name of a student
# Print out rank of that student
# Distinction: 80-100
# Merit: 60-79
# Pass: 40-59
# Fail: 0-39

name = input('Enter student name: ')
grade = int(input('Enter grade: '))

if grade >= 80:
    print('{} ranked as Distinction'.format(name))
elif grade >= 60:
    print('{} ranked as Merit'.format(name))
elif grade >= 40:
    print('{} ranked as Pass'.format(name))
else:
    print('{} ranked as Fail'.format(name))
    
# Do it again but check grade reversely