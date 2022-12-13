import turtle

class Square:   #[Jenna]
    def __init__(self):
        self.__square = turtle.Turtle(visible = False)

        self.__square.shape("square")
        self.__square.color("grey")
        self.__square.speed(1)
        self.__square.penup()
        self.__square.setheading(180)

        self.__distance = 10
        self.__angle = 90

    def show(self):
        self.__square.showturtle()

    def move(self):
        self.__square.goto(self.__square.pos()[0] + self.__distance, self.__square.pos()[1] + self.__distance)
