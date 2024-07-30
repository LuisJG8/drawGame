import tkinter
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

t.shape("turtle")
t.color("blue")

def move_up():
    t.forward(20)

def move_backward():
    t.backward(20)

def move_left():
    t.left(20)

def move_right():
    t.right(20)

screen.onkey(key="w", fun=move_up)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="a", fun=move_right)
screen.listen()


screen.exitonclick()