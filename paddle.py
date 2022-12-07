import turtle

class Paddle:
    #self.__player1Pos = (-10, 0)
    #self.__player2Pos = (10, 0)

    def __init__(self, xPos):
        self.__distance = 20
        self.__paddle = turtle.Turtle(visible = False)

        self.__paddle.penup()
        self.__paddle.setx(xPos)
        self.__paddle.shape("square")
        self.__paddle.setheading(90)
        self.__paddle.shapesize(1, 6)
        self.__paddle.color("grey")
        self.__paddle.speed(0)

    def show(self):
        self.__paddle.showturtle()

    def moveUp(self):
        self.__paddle.forward(self.__distance)

    def moveDown(self):
        self.__paddle.backward(self.__distance)
