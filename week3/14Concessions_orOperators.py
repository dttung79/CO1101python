name = input("What is your name? ")

student_str = input("Are you a student [y/n]? ")
is_student = student_str.lower() in ("y", "yes")

age_str = input("How old are you? ")
age = int(age_str)

message = f"Hello {name}"

if name != 'Chris' or not is_student or 18 < age <= 65:
    message += " - sorry, you must pay the regular price"
else:
    if name == 'Chris':
        discount = 30
    elif is_student and (age <= 18 or age > 65):
        discount = 20
    elif is_student or (age <= 18 or age > 65):
        discount = 10
    
    message += f" - congratulations, you are entitled to a {discount}% discount"

print(message)

print()
input("Press return to continue ...")
