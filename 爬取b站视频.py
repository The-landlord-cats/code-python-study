from turtle import *


def curvemove():
    for i in range(200):
        right(1)
        forward(1)


setup(600, 600, 400, 400)
hideturtle()
pencolor('black')
fillcolor("red")
pensize(2)
begin_fill()
left(140)
fd(111.65)
curvemove()
left(120)
curvemove()
fd(111.65)
end_fill()
penup()
goto(-27, 85)
pendown()
done()
