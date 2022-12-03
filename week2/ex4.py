# Format output string


# enter 3 grades
programming_grade = float(input('Enter programming foundation grade: '))
software_grade = float(input('Enter software engineering grade: '))
networking_grade = float(input('Enter networking grade: '))

avg_grades = (programming_grade + software_grade + networking_grade) / 3

print('{:<20s}:{:>10.2f}'.format('Programming grade', programming_grade))
print('{:<20s}:{:>10.2f}'.format('Software grade', software_grade))
print('{:<20s}:{:>10.2f}'.format('Networking grade', networking_grade))
print('{:<20s}:{:>10.2f}'.format('Average grade', avg_grades))