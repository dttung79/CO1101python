a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

is_all_positive = a > 0 and b > 0 and c > 0
is_2sides_gt_other = a + b > c and a + c > b and b + c > a

if not is_all_positive:
    print('Side must be positive')
elif not is_2sides_gt_other:
    print('Sum of 2 sides must be greater than the other side')
else:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('Area is', s)