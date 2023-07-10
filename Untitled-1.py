from turtle import *

#we want to paint a house

#step 1: draw a square
speed(5)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#darwing a door

forward(70)
color("red")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("green")
right(150)
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()


goto(200,200)
pendown()
left(30)
forward(120)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(54)
right(91)
forward(123)
pendown()
right(90)
forward(203)
right(90)
forward(120)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)


exitonclick()