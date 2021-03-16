# piemers, kas parada funkcijas tracer() darbibu
# so skatiit kopaa ar trace_02.py
import turtle

def draw_square(d) :        # funkcija uzzimee kvadratu
    for side in range(4) :
        d.forward(100)
        d.left(90)

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)            # neatjaunot attelu automaatiski

felix = turtle.Turtle()
felix.speed(0)
felix.width(3)
felix.hideturtle()          # paslepj rupuci, lai redzetu tikai zimejumu

felix.penup()
felix.goto(-350, 0)
felix.pendown()

k = 0.04
for i in range(int(600 // k)):
    felix.clear()           # izdzes ieprieksejo zimejumu
    draw_square(felix)
    screen.update()         # parada jau uzzimetu kvadratu (viens kadrs)
    felix.forward(k)

screen.exitonclick()
