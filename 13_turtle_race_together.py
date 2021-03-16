import turtle
from random import randint

window = turtle.Screen()
window.setup(600, 500)
window.title('Ninja Turtle Race')
window.tracer(0)

field = turtle.Turtle()
field.hideturtle()

field.penup()
field.goto(-60, 180)
field.color("orange")
field.write("Turtle Race", font=("Century Gothic", 20, 'bold'))
field.goto(-140, 140)

# Zimejam starta liniju
field.write(0, align="center")
field.right(90)
field.forward(10)
field.pendown()
field.pensize(5)
field.forward(140)
field.penup()
field.backward(150)
field.left(90)
field.forward(20)
field.pensize(0)

# Linijas no 1 lidz 14
for step in range(1, 15):
    field.write(step, align = "center")
    field.right(90)
    field.forward(10)
    field.pendown()
    for dash in range(5):
        field.forward(20)
        field.penup()
        field.forward(10)
        field.pendown()
    field.penup()
    field.backward(160)
    field.left(90)
    field.forward(20)

# Finisa linija
field.write(15, align="center")
field.right(90)
field.forward(10)
field.pendown()
field.pensize(5)
field.forward(140)

window.tracer(1)

colors = ["blue", "red", "orange", "violet"]
names = ["Leonardo", "Raphael", "Michelangelo", "Donatello"]
turtles = []
n = 4       # кол-во черепах
st_x, st_y = -140, 100
for i in range(n):
    ada = turtle.Turtle()
    ada.color(colors[i])
    ada.shape("turtle")
    ada.penup()
    ada.goto(-160, st_y - i * 30)
    ada.write(names[i], align="right")
    ada.goto(st_x, st_y - i * 30)
    ada.pendown()
    ada.distance(st_x, st_y - i * 30)
    turtles.append(ada)

#for i in range(n):
#    for turn in range(10):
#       turtles[i].right(36)

dist = [0]
while max(dist) < 300:
    dist = []
    for i in range(n):
        turtles[i].forward(randint(4, 5))
        dist.append(turtles[i].distance(st_x, st_y - i * 30))
    print(dist)

    if max(dist) >= 300:
        if dist.count(max(dist)) > 1:
            print("It's a DRAW")
            turtles[dist.index(max(dist))].write(f"         It's a DRAW!", align="left")
        else:
            print("WINNER", names[dist.index(max(dist))], turtles[dist.index(max(dist))].distance(st_x, st_y - dist.index(max(dist)) * 30))
            turtles[dist.index(max(dist))].write(f"         {names[dist.index(max(dist))]} wins!", align="left")
            break


turtle.exitonclick()
