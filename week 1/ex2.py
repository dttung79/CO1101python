import turtle as t

# $$$$ Drawing a car $$$$ #

# Move to the starting point
t.penup()
t.goto(-200, 0)

# Draw the car body
t.pendown()
t.forward(100)
t.penup()
t.forward(100)

t.left(90) # Turn left to draw a place for the first wheel
t.pendown()
t.circle(50, 180)
t.left(90) # Turn left to draw the base.
t.penup()
t.forward(100)
t.pendown()
t.forward(100)
t.penup()
t.forward(100)
t.left(90) # Turn left to draw a place for the second wheel
t.pendown()
t.circle(50, 180)
t.left(90) # Turn left to draw the base.
t.penup()
t.forward(100)
t.pendown()
t.forward(50)

# Draw upper part of the car
t.left(90)
t.forward(100)
# Draw the back window
t.left(45)
t.forward((2*(50**2))**0.5) # Can you explain this line?
t.left(45)
t.forward(250)
# Draw the front window
t.left(45)
t.forward((2*(50**2))**0.5)
# Draw the hood
t.right(45)
t.forward(100)
t.left(90)
t.forward(100)

t.exitonclick()