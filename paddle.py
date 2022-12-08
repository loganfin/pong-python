import turtle

class Paddle:
    def __init__(self, xPos):
        self.__distance = 20
        self.__paddle = turtle.Turtle(visible = False)

        self.__paddle.speed(0)
        self.__paddle.penup()
        self.__paddle.setx(xPos)
        self.__paddle.shape("square")
        self.__paddle.setheading(90)
        self.__paddle.shapesize(1, 6)
        self.__paddle.color("grey")

    def show(self):
        self.__paddle.showturtle()

    def moveUp(self):
        self.__paddle.forward(self.__distance)

    def moveDown(self):
        self.__paddle.backward(self.__distance)
