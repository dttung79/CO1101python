# for i in range(1, 10, 2):
#     print(i, end=' ')

# print()

# for i in range(1, 10):
#     if i % 2 == 0:
#         break
#     print(i, end=' ')

# for i in range(10):
#     n = int(input("Enter a number: "))
#     print(n)
#     answ = input("Do you want to continue? (y/n) ")
#     if answ.lower() == 'n':
#         break

counter = 0
while counter < 10:
    n = int(input("Enter a number: "))
    print(n)
    counter += 1
    answ = input("Do you want to continue? (y/n) ")
    if answ.lower() == 'n':
        break