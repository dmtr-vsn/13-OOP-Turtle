# piemers, kas parada funkcijas tracer() darbibu
# so skatiit kopaa ar trace_03.py
import turtle

def draw_square(d) :         # funkcija uzzimee kvadratu
    for side in range(4) :
        d.forward(100)
        d.left(90)

screen = turtle.Screen()    # izveido jaunu zimejuma logu
screen.setup(500,300)       # 500 x 500 loga izmeri

felix = turtle.Turtle()       
felix.speed(0)              # iestata atrumu

felix.penup()               
felix.goto(-350, -100)         # ziimeesanu saak aarpus ekrana
felix.pendown()

#turtle.tracer(n=2)
k = 4
for i in range(int(600 // k)):  
    felix.clear()           # nodzes ieprieksejo ziimejumu
    draw_square(felix)      # zime kvadratu
    felix.forward(k)        # parvieto nedaudz uz prieksu

screen.exitonclick()
