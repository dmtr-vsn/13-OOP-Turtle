'''
import turtle

window = turtle.Screen()
window.setup( 800, 600 )
window.title( 'RG' )

t = turtle.Turtle()
# t.hideturtle()
t.pencolor('blue')
t.speed(3)

# "R"
import math

t.lt(90)
t.fd(100)
t.rt(90)
t.circle(-30 ,180)
t.lt(130)
t.fd(math.sqrt(40 *40 + 30 *30))

# "G"
t.penup()
t.goto(90 ,100)
t.pendown()

t.seth(0)
t.circle(-50 ,-180)
t.rt(90)
t.fd(40)
t.lt(90)
t.fd(30)

turtle.exitonclick()

'''
import turtle
window = turtle.Screen()
window.setup( 600, 400 )
window.title('Drawing S' )

felix = turtle.getturtle()
felix.hideturtle()

felix.color( 'red', 'DarkTurquoise' ) # fona kraasa, aizpildijuma krasa



felix.penup()
felix.setposition(0,-90)
felix.pendown()
felix.right(40)
felix.speed(0)

for i in range(210):
    turtle.left(1)
    felix.forward(1)

for i in range(200):
    turtle.right(1)
    felix.forward(1)



turtle.exitonclick()