import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


draw_spiral(myTurtle, 100)
myWin.exitonclick()
