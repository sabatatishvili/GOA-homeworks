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







name= "saba"
surname= "tatishvili"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმანიჭებელი სიმბოლო
# "saba" არის ცვლადისთვის მნიშვნელობა

#print(name)
# print ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი
 
name = "saba" #ეს არის str (string) ტიპის ცვლადი
age = 15 #ეს არის int (integer) მთელი რიცხვი
height = 59,5 #ეს არის float ტიპის ცვლადი (ათწილადი)

knows_programming = True #True ან False
is_ugly = False #snakecase (უბრალოდ წერის სტილი სტანდარტულად)
isUgly = False #ჯავასკრიპტული camelcase


#print(name + surname)


#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
#print(name + age)


#Print(type(age))
#Print(type(name))
#Print(type(surname))
#Print(type(height))
#Print(type(knows_programming)))


#print(name + " " + str(age))

print(name + " " + str(surname) + " " + str(age) + " " + str(height) + " " + str(knows_programming)) 