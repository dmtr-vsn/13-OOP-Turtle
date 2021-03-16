import turtle

window = turtle.Screen()

window.setup(600, 400)

window.title("My first Turtle Graphics Program")

window.bgcolor("white")

#felix = turtle.getturtle()
# передвижение по точкам (двигаться в точку 100, 0)
#felix.setposition(100, 0)
#felix.setposition(100, 100)
#felix.setposition(0, 100)
#felix.setposition(0, 0)

felix = turtle.getturtle()
#felix.hideturtle()      # скрыть значок черепашки
felix.resizemode("user")
turtle.shapesize(1, 1)
felix.shape("turtle")     # установить значок черепашки
felix.fillcolor('green')

# izveido kvadratu, mainot relativo poziciju
felix.pencolor("CadetBlue")     # цвет линии
felix.begin_fill()              # заливка цветом
felix.pensize(5)                # размер линии
felix.forward( 100 )    # двигаться вперед на 100 пикс.
felix.left( 90 )        # повернуться влево на 90 градусов
felix.penup()           # поднять ручку - не рисовать
felix.forward( 100 )
felix.left( 90 )
felix.pendown()         # опустить ручку - рисовать
felix.forward( 100 )
felix.left( 90 )
felix.forward( 100 )
felix.end_fill()

turtle.exitonclick()

