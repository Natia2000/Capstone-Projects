from turtle import *


#we want to paint a house
shape("turtle")
#speed(30)
#step 1: draw a square
width(12)
color("purple")
forward(200)
left (90)

forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)
#end of square

#drawing a door

forward(70)
begin_fill()
color ("orange")
left(90)
forward(120)    #height of the door
right (90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of a roof

#drawing a window
color("purple")
begin_fill()
goto(0,180)
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#end of a left window

#drawing a right window

color("purple")

penup()
goto(200,180)
pendown()
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#end of right window

#drawing a handle

color("black")
penup()
goto(120,75)
pendown()
left(90)
forward(20)

#end of a handle

#drawing a chandelier

color("black")
penup()
goto(100,200)
pendown()
left(180)
forward(50)
shape("circle")

#end of a chandelier




exitonclick ()