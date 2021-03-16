import random
import math
import turtle
random.seed(100)


window = turtle.Screen()
window.setup(600, 500)
window.title('Circle')

axis_x = turtle.Turtle()
axis_x.penup()
axis_x.goto(-150, 0)
axis_x.pendown()
axis_x.forward(300)
axis_x.write("X", align="center")

axis_y = turtle.Turtle()
axis_y.penup()
axis_y.goto(0, -150)
axis_y.left(90)
axis_y.pendown()
axis_y.forward(300)
axis_y.write("Y", align="center")

# 1. izveidot sarakstus ar x un y koordinatem

n = 10
x = []
y = []

#[0;9]
for i in range(n):
    x.append(random.randint(-100, 100))
    y.append(random.randint(-100, 100))

# 2. izvadit punktu koordinates
for i in range(n):
    print(f'({x[i]}, {y[i]})', end= ' ')
print()

# uzzime punktus
felix = turtle.Turtle()
felix.hideturtle()
for i in range(n):
    felix.penup()
    felix.goto(x[i], y[i])
    felix.pendown()
    felix.dot("red")

# 3. atrast taisnstura stura koordinates
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

aug_k_sturis = (x_min, y_max)
aug_l_sturis = (x_max, y_max)
ap_k_sturis = (x_min, y_min)
ap_l_sturis = (x_max, y_min)
print(f'Taisnstura sturi: {aug_k_sturis}, {aug_l_sturis}, {ap_k_sturis}, {ap_l_sturis}')

# uzzime taisnsturu
for i in range(n):
    felix.penup()
    felix.goto(aug_k_sturis)
    felix.pendown()
    felix.goto(aug_l_sturis)
    felix.goto(ap_l_sturis)
    felix.goto(ap_k_sturis)
    felix.goto(aug_k_sturis)

# 4. atrast taistura laukumu
laukums = (x_max - x_min) * (y_max - y_min)
print(f'Taisnstura laukums: {laukums}')

# 5. atrast rinka radiusu un laukumu
punktu_attalumi = []
for i in range(n):
    attalums = math.sqrt(x[i] ** 2 + y[i] ** 2)
    punktu_attalumi.append(round(attalums,2))
print(punktu_attalumi)

radiuss = max(punktu_attalumi)

# uzzime taisnsturu
felix.penup()
felix.goto(0, -radiuss)
felix.pendown()
felix.circle(radiuss)

#laukums = round(math.pi * radiuss ** 2,2)
laukums = math.pi * radiuss ** 2
print(f'Rinka radiuss: {radiuss}')
print(f'Rinka laukums: {laukums:.2f}')

turtle.exitonclick()