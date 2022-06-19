from turtle import Turtle
from random import randint

leo = Turtle
leo.color('green')
leo.shape('turtle')
leo.penup()
leo.goto(-160,100)
leo.pendown()

Dona = Turtle
Dona.color('purple')
Dona.shape('turtle')
Dona.penup()
Dona.goto(-160,70)
Dona.pendown()

Raph = Turtle
Raph.color('red')
Raph.shape('turtle')
Raph.penup()
Raph.goto(-160,40)
Raph.pendown()

Mike = Turtle
Mike.color('orange')
Mike.shape('turtle')
Mike.penup()
Mike.goto(-160,10)
Mike.pendown()

for movement in rang(100):
    leo.forward(random(1,5))
    Dona.forward(random(1,5))
    Raph.forward(random(1,5))
    Mike.forward(random(1,5))