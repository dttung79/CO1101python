import turtle as t
def draw_polygon(n, color, pen_width):
    # TODO: draw a regular polygon with n sides, using the given color and pen width
    angle = 360 / n
    t.color(color)
    t.pensize(pen_width)
    
    for i in range(n):
        t.forward(100)
        t.left(angle)

def draw_polygons(n_poloygons, n_sides, color, pen_width):
    angle = 360 / n_poloygons
    for n in range(n_poloygons):
        draw_polygon(n_sides, color, pen_width)
        t.left(angle)

t.speed(200)
draw_polygons(12, 5, "red", 2)
t.exitonclick()