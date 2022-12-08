import turtle

class Square:   #[Jenna]
    def __init__(self):
        self.__square = turtle.Turtle()

        self.__square.hideturtle()
        self.__square.shape("square")
        self.__square.color("grey")
        self.__square.speed("slowest")
        self.__square.penup()
        self.__square.showturtle()

        self.__distance = 1

    def move(self):
        for i in range(10):
            self.__square.up(self.__distance)
