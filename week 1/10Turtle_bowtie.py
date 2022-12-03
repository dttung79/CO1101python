# draw a bowtie

import turtle as t

ps = int(input('Choose pen size: '))
pcolor = input('Choose pen color: ')

t.pensize(ps)
t.penup()
t.goto(-200, -100)
t.pendown()
t.fillcolor(pcolor)

t.begin_fill()
t.goto(-200, 100)
t.goto(200, -100)
t.goto(200, 100)
t.goto(-200, -100)
t.end_fill()

t.exitonclick()
