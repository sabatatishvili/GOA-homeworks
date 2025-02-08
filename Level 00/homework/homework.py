from turtle import *

#print("saba tatishvili")

print(5)     #integer   int
print("5")   #string    #str

print(5 + int("5"))

#asdasdasdasd

#we want to paint a house

#step 1: draw a square
shape("turtle")
speed(15)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

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

penup()
goto(200,200)
pendown()

color("purple")
left(30)
forward(70)

color("brown")
right(90)
forward(60)
right(90)
forward(65)
right(90)
forward(60)
right(90)
forward(60)


penup()
goto(0, 200)
pendown()

color("brown")



left(90)
forward(60)
right(90)
forward(65)
right(90)
forward(60)
right(90)
forward(60)

right(90)
forward(60)
right(180)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward (60)

penup()
goto(200, 200)
pendown()

forward(60)
left(90)
forward(37)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)


exitonclick()