import turtle
bob=turtle.Turtle()
bob.speed(0)
bob.width(2)
turtle.bgcolor("light blue")

for times in range(25):
     for colours in ["firebrick", "firebrick", "firebrick", "sienna", "sienna", "sienna", "sienna"]:
        bob.color(colours)
        bob.circle(10,times*3,10+7)
        bob.circle(100)
        bob.left(1)
    
for i in range(5):
     for colours in ["coral", "coral", "coral", "coral", "orange red", "orange red", "orange red"]:
        bob.color(colours)
        bob.pensize(3)
        bob.left(12)
        bob.forward(200)
        bob.left(90)
        bob.forward(200)
        bob.left(90)
        bob.forward(200)
        bob.left(90)
        bob.forward(200)
        bob.left(90)

bob.penup()
bob.goto(37,-30)
bob.pendown()

for times in range (25):
     bob.color("goldenrod")
     bob.begin_fill()
     bob.circle(50)
     bob.end_fill()
    

bob.color("forest green")
bob.width(18)
bob.penup()
bob.right(180)
bob.forward(200)
bob.left(45)
bob.left(85)
bob.forward(75)
bob.pendown()
bob.right(95)
bob.forward(400)

bob.penup()
bob.goto(-300,-300)
bob.pendown()

for i in range(5):
     for colours in ["coral", "coral", "coral", "coral", "orange red", "orange red", "orange red"]:
        bob.color(colours)
        bob.pensize(1)
        bob.left(12)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)

bob.penup()
bob.goto(300,-300)
bob.pendown()

for i in range(5):
     for colours in ["coral", "coral", "coral", "coral", "orange red", "orange red", "orange red"]:
        bob.color(colours)
        bob.pensize(1)
        bob.left(12)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)

bob.penup()
bob.goto(-300,300)
bob.pendown()

bob.penup()
bob.goto(-300,300)
bob.pendown()

for i in range(5):
     for colours in ["coral", "coral", "coral", "coral", "orange red", "orange red", "orange red"]:
        bob.color(colours)
        bob.pensize(1)
        bob.left(12)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)

bob.penup()
bob.goto(300,300)
bob.pendown()


for i in range(5):
     for colours in ["coral", "coral", "coral", "coral", "orange red", "orange red", "orange red"]:
        bob.color(colours)
        bob.pensize(1)
        bob.left(12)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)
        bob.forward(100)
        bob.left(90)






