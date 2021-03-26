import turtle
import random

#ekraani seaded
aken = turtle.Screen()
aken.setup(300,300) #x,y
aken.bgcolor("gray")
aken.title("liigutame konna")

# x=100
# a=144
# värvid = ["lime","red","orange","blue"]

#ülesanne 1-------------------------
# for i in range(8):
#     turtle.color(random.choice(värvid))
#     turtle.fd(x)
#     turtle.bk(x)
#     turtle.lt(a)
# -------------------------------

pikkus = 50
a = 120
for i in range(6):    
    turtle.right(60)       
    for i in range(3):
        turtle.fd(100)
        turtle.right(a)


# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)

