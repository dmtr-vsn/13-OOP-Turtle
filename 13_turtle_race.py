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
n = 4       # turtles quantity
st_x, st_y = -140, 100      # turtles start position. Finish line at (160, 100), because distance between lines is 20 pt.
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

for i in range(n):
    for turn in range(10):
       turtles[i].right(36)

dist = [0]      # distance walked by turtles
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



''' #FIRST TRY
import turtle
from random import randint

field = turtle.Turtle()

field.speed(0)
field.penup()
field.goto(-140, 140)
for step in range(1, 16):
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


# 1 =========================

leonardo = turtle.Turtle()
leonardo.color("blue")
leonardo.shape("turtle")

leonardo.penup()
leonardo.goto(-180, 100)
leonardo.write("Leonardo", align = "right")

leonardo.goto(-160, 100)
leonardo.pendown()

# 2 =========================

raphael = turtle.Turtle()
raphael.color("red")
raphael.shape("turtle")

raphael.penup()
raphael.goto(-180, 70)
raphael.write("Raphael", align = "right")

raphael.goto(-160, 70)
raphael.pendown()

# 3 =========================

michelangelo = turtle.Turtle()
michelangelo.color("orange")
michelangelo.shape("turtle")

michelangelo.penup()
michelangelo.goto(-180, 40)
michelangelo.write("Michelangelo", align = "right")

michelangelo.goto(-160, 40)
michelangelo.pendown()

# 4 =========================

donatello = turtle.Turtle()
donatello.color("violet")
donatello.shape("turtle")

donatello.penup()
donatello.goto(-180, 10)
donatello.write("Donatello", align = "right")

donatello.goto(-160, 10)
donatello.pendown()


leonardo.right(360)

for turn in range(100):
    leonardo.forward(randint(1, 5))
    raphael.forward(randint(1, 5))
    michelangelo.forward(randint(1, 5))
    donatello.forward(randint(1, 5))
    
turtle.exitonclick()
'''