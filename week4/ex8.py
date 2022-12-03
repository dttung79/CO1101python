import turtle as t
n = int(input('Enter n: '))

angle = 360 // n

for i in range(n):
    t.forward(100)
    t.goto(0, 0)
    t.left(angle)
    
t.exitonclick()