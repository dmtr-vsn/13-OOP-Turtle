
'''
import turtle
def draw_square(d) : # funkcija uzzimee kvadratu
    for side in range(4) :
        d.forward(100)
        d.left(90)
screen = turtle.Screen() # izveido jaunu zimejuma logu
screen.setup(500,500) # 500 x 500 loga izmeri
felix = turtle.Turtle()

felix.speed(0) # iestata atrumu
felix.penup()
felix.goto(-350, 0) # ziimeesanu saak aarpus ekrana
felix.pendown()
k = 4 # kvadraata parvietojums starp kadriem
for i in range(int(600 // k)):
    felix.clear() # nodzes ieprieksejo ziimejumu
    draw_square(felix) # zime kvadratu
    felix.forward(k) # parvieto nedaudz uz prieksu
screen.exitonclick()
'''

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

k = 0.04                    # kvadraata parvietojums starp kadriem
for i in range(int(600 // k)):
    felix.clear()           # izdzes ieprieksejo zimejumu
    draw_square(felix)
    screen.update()         # parada jau uzzimetu kvadratu (viens kadrs)
    felix.forward(k)

screen.exitonclick()