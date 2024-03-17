from turtle import *

#we want to paint a house

#step 1: drawing a square
shape("turtle")
speed(30)
width(7)

begin_fill()
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

#end of square

#step 2: drawing a door
begin_fill()
left(90)
forward(70)   
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)   #lenght of the door
right(90)
forward(120)
right(90)
forward(60)
left(90)
end_fill()

#end of the door

#step 3: drawing a roof
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

#end of roof

#stepn 4: drawing windows
penup()
goto(10, 190)
pendown()

begin_fill()
width(5)
left(120)
color("light blue")
forward(50)   
right(90)
forward(60)   
right(90)
forward(50)
right(90)
forward(60)
right(90)
end_fill()

width(5)
color("orange")
forward(50)   
right(90)
forward(60)   
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(25)
right(90)
color("brown")
forward(60)
left(180)
forward(30)
left(90)
forward(25)
left(180)
forward(50)

penup()
goto(140, 190)
pendown()

begin_fill()
color("light blue")
forward(50)   
right(90)
forward(60)   
right(90)
forward(50)
right(90)
forward(60)
right(90)
end_fill()

color("orange")
forward(50)   #lenght of the window
right(90)
forward(60)   #height of the window
right(90)
forward(50)
right(90)
forward(60)
right(90)
forward(25)
right(90)
color("brown")
forward(60)
left(180)
forward(30)
left(90)
forward(25)
left(180)
forward(50)

#end of the window

#step 5: drawing a meadow
penup()
goto(0, -5)
pendown()

color("green")
begin_fill()
forward(1000)
right(90)
forward(1000)
right(90)
forward(2000)
right(90)
forward(1000)
end_fill()

#step 6: drawing a handle
penup()
goto(78, 58)
color("brown")
shape("circle")
pendown()

exitonclick()

#end of the house