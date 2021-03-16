#from turtle import *
import turtle
from random import randint

window = turtle.Screen()
window.tracer(0)        # neatjaunot attelu automaatiski
race = turtle.Turtle()
race.speed(0)
# saakuma x un y koordinaates uzraksta veidosanai
st_x = -60
st_y = 180

race.penup()
race.goto(st_x, st_y)
race.color('orange')
race.write("Turtle race", font=('Century Gothic', 20, 'bold'))

# saakuma x un y koordinaates skrejcelja ziimeesanai
st_x = -140
st_y = 140

# skrejcelja izveidosana
race.penup()
race.goto(st_x, st_y)
race.color("grey")
for step in range(16):
    race.write(step, align='center')
    race.right(90)
    race.forward(10)
    for i in range(10):
        race.pendown()
        race.forward(10)
        race.penup()
        race.forward(8)
    race.backward(190)
    race.left(90)
    race.forward(20)
race.backward(20) # jo ciklaa peedeejaa iteraacijaa pagaaja 20 vieniibas uz prieksu

# finisa liinijas koordinaates, izmantos, lai noskaidrotu uzvareetaaju
#finish_line_x = race.xcor()
finish_line_x = 160
print(finish_line_x)

# starta liinijas uzziimeesana
race.penup()
race.goto(st_x-2, st_y)
race.color("orange")
race.begin_fill()
race.right(90)
race.forward(10)
race.pendown()
race.forward(172)
race.left(90)
race.forward(5)
race.left(90)
race.forward(172)
race.left(90)
race.forward(5)
race.end_fill()

race.setheading(0)

# finisa liinijas uzziimeesana
race.penup()
race.goto(finish_line_x + 2, st_y)
race.begin_fill()
race.right(90)
race.forward(10)
race.pendown()
race.forward(172)
race.right(90)
race.forward(5)
race.right(90)
race.forward(172)
race.right(90)
race.forward(5)
race.end_fill()
race.hideturtle()

window.update()         # parada attelu
window.tracer(1)        # neatjaunot attelu automaatiski

# izveido 5 brunurupucus
# saraksts ar brunrupucu vaardiem
names = ['Ada', 'Bob', 'Felix', 'Alex', 'Anna']
# saraksts ar brunrupucu kraasaam
colors = ['red', 'blue', 'green', 'indianred1', 'violet']
# saraksts lai identificetu skrejienu pabeigusos brunrupucus
finished = [False, False, False, False, False]
# tukss saraksts, kuraa ievietos brunrupucus
turtles = []
# pirmaa brunrupuca x un y koordinates
tx = -140
ty = 100
# pirmaa brunrupuca vaarda koordinates
vx = tx - 60
vy = ty - 5
# brunrupucu skaits
n = 5

# brunrupucu vaardu izvietosana
for i in range(0, n):
    text = turtle.Turtle()
    text.color(colors[i])
    text.hideturtle()
    text.penup()
    text.goto(vx, vy)
    text.pendown()
    text.write(names[i], font=('Arial', 10, 'normal'))
    vy -= 30


# brunrupucu izveidosana
for i in range(0, n):
    my_turtle = turtle.Turtle()
    my_turtle.color(colors[i])
    my_turtle.shape('turtle')
    my_turtle.penup()
    my_turtle.goto(tx, ty)
    my_turtle.pendown()
    # brunrupuca pagriesanaa par 360 graadiem
    for k in range(36):
        my_turtle.right(10)
    ty -= 30
    turtles.append(my_turtle)

# skreejiens
win = False
winner = -1
finished_count = 0
first_finished_count = 0
first_x = -1
finished_x = -1

steps = 0
while finished_count < 5:
    for i in range(len(turtles)):
        if not finished[i]:
            turtles[i].forward(randint(1, 5))

        if turtles[i].xcor() >= finish_line_x and not finished[i] and not win:
            print("Win:")
            print(names[i], "steps = ", steps, "coord = ", turtles[i].xcor())
            ('-----------------')
            finished[i] = True
            first_finished_count += 1
            finished_count += 1
            finished_x = turtles[i].xcor()
            # noskaidro, kurs ir uzvareetaajs
            if finished_x > first_x:
                first_x = finished_x
                winner = i
        if turtles[i].xcor() >= finish_line_x and not finished[i]:
            print("Finished:")
            print(names[i], "steps = ", steps, "coord = ", turtles[i].xcor())
            finished[i] = True
            finished_count += 1
#        if turtles[i].xcor() >= finish_line_x and not win:
#            print(names[i])
#            win = True
#            winner = i
    # ir uzvareetaajs
    if first_finished_count > 0 and not win:
        win = True
        # uzvaras pazinosana
        win_x = finish_line_x + 50
        win_y = turtles[winner].ycor() - 5
        text.penup()
        text.goto(win_x, win_y)
        text.pendown()
        text.color(colors[winner])
        text.write(names[winner] + " wins!!!", font=('Arial', 16, 'bold'))
        
    steps += 1

print('-----------------')
print('Winner is ' + names[winner])
print(turtles[winner].xcor())
print(finish_line_x)
window.exitonclick()
