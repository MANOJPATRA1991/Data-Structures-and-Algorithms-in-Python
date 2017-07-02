import turtle
from random import randint


def tree(branch_len, t, x):
    if branch_len > 5:
        t.pensize(x)
        if x == 2:
            t.color("green")
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, x-2)
        t.left(40)
        tree(branch_len - 15, t, x-2)
        t.right(20)
        t.backward(branch_len)
        t.color("brown")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.pensize(10)
    t.color("brown")
    tree(75, t, 10)
    myWin.exitonclick()


main()
