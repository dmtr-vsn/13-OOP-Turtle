import turtle

window = turtle.Screen()
window.setup(600, 400)
window.title("My second Turtle Graphics Program")
window.bgcolor("white")


felix = turtle.getturtle()

'''
# N-sturis ===============
felix.fillcolor('Green')
felix.pencolor("CadetBlue")
felix.pensize(5)

felix.begin_fill()
n = 3
for i in range(n):
    felix.forward( 80 )
    felix.left(360 / n)
felix.end_fill()

#turtle.exitonclick()

# W burta =================
felix.reset()
felix.pencolor("Blue")
felix.pensize(5)

felix.right( 60 )
felix.forward( 80 )
felix.left(120)
felix.forward( 20 )
felix.penup()
felix.setposition( 20, 0 )
felix.pendown()
felix.right( 120 )
felix.forward( 80 )
felix.left(120)
felix.forward( 80 )

#turtle.exitonclick()


#====A BURTS============
felix.reset()
felix.pencolor( 'red' )
felix.pensize( 5 )          # konturas biezums
felix.penup()
# izveido A burtu, mainot absoluuto poziciju
felix.setposition( -100, -100 )
felix.pendown()
felix.setposition( 0, 150 )
felix.setposition( 100, -100 )
felix.penup()
felix.setposition( -64, -10 )
felix.pendown()
felix.setposition( 64, -10 )

#turtle.exitonclick()

# N burts ===============
felix.reset()
fig=turtle.getturtle()
fig.pencolor('blue')
fig.pensize(10)
fig.penup()
fig=turtle.getturtle()
fig.setpos(70,-120)
N = ((70,-20),(120,-120),(120,-20))
fig.pendown()
for i in N :
    fig.setposition(i)

#turtle.exitonclick()

# Iniciali =================

felix.reset()
felix.pencolor("red")
felix.pensize(5)

felix.penup()
felix.setposition( -100, 0 )
felix.pendown()
felix.setposition(-100, -100)
felix.setposition(-70, -100)
felix.setposition(-50, -50)
felix.setposition(-70, 0)
felix.setposition(-100, 0)

felix.penup()
felix.setposition( -30, 0 )
felix.pendown()
felix.setposition(0, -100)
felix.setposition(30, 0)

#turtle.exitonclick()

# N-staru zvaigzne =================
'''

felix.reset()
felix.pencolor("black")
felix.pensize(5)

l = 50
n = 5

felix.speed(0)
for i in range(n):
    felix.forward(l)
    felix.left( 180 - 360/n/2 )
    felix.forward(l)
    felix.right(180 - 360/n - 360/n/2)


felix.penup()
felix.setposition( l * 4, 0 )
felix.pendown()
for i in range(n):
    felix.left(180)
    felix.forward(l)
    felix.right(180 - 360 / n )
    felix.forward(l)

#turtle.exitonclick()

# 3 uzdevums =================

import random
turtle.colormode(255)
n = 5
k = 10
l = 10  # linijas garums

krasu_saraksts = [[random.randint(1, 255) for i in range(3)] for j in range(k)]

felix.pensize(3)
for i in range(k):
    felix.pencolor(random.choice(krasu_saraksts))
    for i in range(n):
        felix.forward(l)
        felix.left(360 / n)
    l += 5

turtle.exitonclick()

'''

#Ēriks
# 3. uzdevums
n = 5
k = 10
turtle.colormode(255)
felix.pensize(5)
felix.hideturtle()
from random import randint
for i in range(k):
    felix.pencolor(randint(0,255),randint(0,255),randint(0,255))
    for j in range(n):
        felix.forward(5 * i)
        felix.left(360 / n)

# 2. uzdevums
n = 10
felix.color('cyan','cyan')
felix.begin_fill()
felix.hideturtle()
angle = 180 - (180/n)
turtle.speed(0)

for i in range(n):
    turtle.forward(100)
    turtle.right(angle)

felix.end_fill()


turtle.exitonclick()

'''

