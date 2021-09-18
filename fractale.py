from turtle import *
import turtle

speed(100)
right(30)
shape('triangle')
penup()


def sierpinski(length, order):
    if order == 0:
        stamp()
    else:
        for i in range(0, 3):
            forward(length)
            sierpinski(length/2, order-1)
            back(length)
            left(120)


print(sierpinski(90, 4))


# import turtle


# def draw_sierpinski(length, depth):
#     if depth == 0:
#         for i in range(0, 3):
#             t.fd(length)
#             t.left(120)
#     else:
#         draw_sierpinski(length/2, depth-1)
#         t.fd(length/2)
#         draw_sierpinski(length/2, depth-1)
#         t.bk(length/2)
#         t.left(60)
#         t.fd(length/2)
#         t.right(60)
#         draw_sierpinski(length/2, depth-1)
#         t.left(60)
#         t.bk(length/2)
#         t.right(60)


# window = turtle.Screen()
# t = turtle.Turtle()
# draw_sierpinski(100, 2)
# window.exitonclick()
